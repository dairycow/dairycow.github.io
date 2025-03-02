# My Jekyll Website

This is a simple Jekyll website project that serves as a starting point for creating a blog or personal website.

## Project Structure

- `_config.yml`: Configuration settings for the Jekyll site.
- `_posts/`: Contains blog posts in markdown format.
  - `2023-01-01-welcome-to-jekyll.md`: The first blog entry.
- `_layouts/`: Contains layout files for the website.
  - `default.html`: The default layout structure.
- `_includes/`: Contains reusable HTML snippets.
  - `header.html`: The header section of the website.
- `_sass/`: Contains Sass stylesheets.
  - `main.scss`: Main stylesheet for the website.
- `assets/`: Contains static assets like CSS files.
  - `style.css`: Additional styles for the website.
- `index.html`: The main entry point of the website.
- `README.md`: Documentation for the project.

## Getting Started

To set up this Jekyll website locally, follow these steps:

1. **Install Jekyll**: Make sure you have Ruby and Bundler installed. Then, install Jekyll by running:
   ```
   gem install jekyll bundler
   ```

2. **Clone the Repository**: Clone this repository to your local machine:
   ```
   git clone https://github.com/yourusername/my-jekyll-website.git
   ```

3. **Navigate to the Project Directory**:
   ```
   cd my-jekyll-website
   ```

4. **Install Dependencies**: Run the following command to install the necessary gems:
   ```
   bundle install
   ```

5. **Serve the Website**: Start the Jekyll server with:
   ```
   bundle exec jekyll serve
   ```

6. **View the Website**: Open your browser and go to `http://localhost:4000` to view your Jekyll website.

## Customization

You can customize the website by editing the following files:

- Update `_config.yml` to change the site title and description.
- Add new posts in the `_posts` directory.
- Modify the layout in `_layouts/default.html`.
- Change styles in `_sass/main.scss` or `assets/style.css`.

## License

This project is licensed under the MIT License.