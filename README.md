# resume-generator
A powerful AI-driven tool designed to streamline your job application process. This tool analyzes your existing work and project experience to automatically generate tailored resumes and professional profiles that align perfectly with your target roles. Instead of spending hours manually adjusting your resume for each application, let AI help you highlight the most relevant experiences and skills, saving you valuable time while maximizing your chances of landing your dream job.

## Development Setup

This project uses `pipenv` for dependency management. Here's how to get started on Windows:

1. First, ensure you have `pipenv` installed:
   ```cmd
   pip install pipenv
   ```

2. Install all dependencies (including development dependencies):
   ```cmd
   pipenv install --dev
   ```

3. Create a `config.json` file based on the example:
   ```cmd
   copy config.json.example config.json
   ```
   Then edit `config.json` to add your Anthropic API key.

4. Activate the virtual environment:
   ```cmd
   pipenv shell
   ```

Now you're ready to start developing! The virtual environment will ensure you have all the necessary packages installed in an isolated environment.

### Common Pipenv Commands (Windows)

- `pipenv install <package>`: Install a new package
- `pipenv uninstall <package>`: Remove a package
- `pipenv lock`: Generate Pipfile.lock
- `pipenv graph`: Show dependency graph
- `pipenv check`: Check for security vulnerabilities
- `pipenv --venv`: check your current env
