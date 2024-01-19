import pandas as pd


def generate_markdown(csv_file, markdown_file, tags_list, specific_authors):
    # Read the CSV file into a DataFrame
    df = pd.read_csv(csv_file)

    # Initialize data_dict with an empty dictionary for each tag and 'All'
    data_dict = {tag: {} for tag in tags_list}
    data_dict["All"] = {}
    all_entries_set = set()
    
    # Process each row
    for index, row in df.iterrows():
        row_tags = row['Tags'].split(';')
        year = str(row['Year'])  # Convert year to string
        unique_id = (row['Title'], row['Author'])
        author_field = row['Author']
        for author in specific_authors:
            if author in author_field:
                author_field = author_field.replace(author, f"<strong>{author}</strong>")
        row['Author'] = author_field

        # Add entry to 'All' if not present
        if unique_id not in all_entries_set:
            all_entries_set.add(unique_id)
            entry = row.drop('Tags').to_dict()
            entry = row.drop('Year').to_dict()
            data_dict["All"].setdefault(year, []).append(entry)

        # Add entry to specific tags
        for tag in tags_list:
            if tag in row_tags:
                entry = row.drop('Tags').to_dict()
                data_dict[tag].setdefault(year, []).append(entry)
                    
    # Write to Markdown file
    with open(markdown_file, 'w', encoding='utf-8') as md_file:
#         md_file.write(
#                         """
#                         ---
#                         layout: publications
#                         title: publications

#                         permalink: /publications/
#                         ---

#                         {:.alert .alert-warning}

#                         <!-- This is a default page. See [configuration]({{ '/docs/configuration/' | relative_url }}) to learn more about **pages**.

#                         To remove this page, you need to:

#                         - Remove `pages/about.md`
#                         - Update `_data/navigation.yml` to remove the link to this page from the top navigation. -->
#                         """
#                         )
        # Buttons for each tag
        for tag in tags_list:
            md_file.write(f"<button onclick=\"showContent('{tag}')\">{tag}</button>\n")

        # Content sections for each tag
        for tag, years_dict in data_dict.items():
            md_file.write(f"<div id='{tag}' class='content' style='display:none;'>\n")
            
            # Sort and iterate through years
            for year in sorted(years_dict.keys(), reverse=True):
                md_file.write(f"<h2>{year}</h2>\n")
                for item in years_dict[year]:
                    for key, value in item.items():
                        md_file.write(f"{key} : {value}<br>\n")
                    md_file.write("<br>\n")
            
            md_file.write("</div>\n")

        # Adding JavaScript for toggle functionality
        md_file.write("<script>\n")
        md_file.write("function showContent(id) {\n")
        md_file.write("  var contents = document.getElementsByClassName('content');\n")
        md_file.write("  for (var i = 0; i < contents.length; i++) {\n")
        md_file.write("    contents[i].style.display = 'none';\n")
        md_file.write("  }\n")
        md_file.write("  document.getElementById(id).style.display = 'block';\n")
        md_file.write("}\n")
        md_file.write("</script>\n")
                    

                    
tags_list = ["All", "HCI", "Trust", "Youth"] #WILL UPDATE IT LATER
author_list =["Seberger, J. S.", "Afsaneh Razi", "Rezvaneh Rezapour"] # WILL UPDATE IT LATER

        
generate_markdown('Publication List.csv', 'Publication_Trial.md', tags_list, author_list)
