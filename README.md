# Video Generator from Python Code

This project allows you to generate a video from a Python code file using syntax highlighting and animation.

## Environment Settings

1. **Clone the repository:**

     ```bash
     https://github.com/Apollo-X1/Code-To-Video.git
     cd Code-To-Video
     ```

2. **Create and activate the virtual environment:**

     ```bash
     python -m venv venv
     source venv/bin/activate # On Windows: venv\Scripts\activate
     ```

3. **Install the necessary libraries:**

     ```bash
     pip install -r requirements.txt
     ```

## Use

1. Place your Python code file in the same folder as the `main.py` script.

2. Make sure your code file is called `pr.py`.

3. Run the script:

     ```bash
     python main.py
     ```

4. Watch the progress and wait for the resulting video to be generated.

## Personalization

- If you want to adjust the font size or make other customizations to the generated images, you can modify the options in the `formatter_options` dictionary in the `main.py` file.

- Remember that you can also modify the resolution and other parameters of the video in the `center_on_canvas` function.

## Credits

This project uses the following libraries:

- `pygments` for syntax highlighting.
- `moviepy` for video generation and manipulation.
- `rich` for the display of the progress bar.

## License

This project is licensed under the APACHE 2.0 License. See the [LICENSE](LICENSE) file for details.
