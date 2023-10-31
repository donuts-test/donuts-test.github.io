# Donuts Colab

This is a Jekyll theme for research project websites. Or your personal blog or lab website. 👩‍🔬 It's mobile-friendly (thanks to [Bootstrap 5](https://getbootstrap.com/docs/5.1/)), free, easy to customize, and designed to work well with [GitHub Pages](https://pages.github.com/).

## Installation

-	Install all Prerequisites

-	Install the jekyll and bundler gems:
        gem install Jekyll bundler 

-	clone the project:
git clone https://github.com/donuts-test/donuts-test.github.io

-	Go into your project directory:
   cd donuts-test.github.io

-	Make the site available on a local server:
        Bundle exec Jekyll serve

-	Browse to http://localhost:4000/


## Preview

[Demo website](https://donuts-test.github.io)




## License

[MIT License](LICENSE)



## Usage

This website makes use of the static website generator [Jekyll](https://jekyllrb.com/) and the [Petridish](https://github.com/peterdesmet/petridish) theme. **Each commit to `main` will automatically trigger a new build on GitHub Pages.** There is no need to build the site locally, but you can by installing Jekyll and running `bundle exec jekyll serve`.

Minor changes can be committed directly to `main`.

Changes requiring review (e.g. new blog posts) should be created in a separate branch and submitted as a pull request. Some guidelines:


## Repo structure

The repository structure follows that of Jekyll websites.

- General site settings: [_config.yml](_config.yml)
- Pages: [pages/](pages/)
- Posts: [_posts/](_posts/)
- Images & static files: [assets/](assets/)
- Top navigation: [_data/navigation.yml](_data/navigation.yml)
- Footer content: [_data/footer.yml](_data/footer.yml)
- Team members: [_data/team.yml](_data/team.yml)
