## Generate icon
 1. Save a small image you want to use as the app icon as a png file.
 2. Install this utility which provides a simple interface for generating an icon icns file from a provided png file: `python3 -m pip install generate-iconset`
 3. Run the utility on your png file to generate your icon file: `/Users/cstout16/Library/Python/3.9/bin/generate-iconset paau2_image.png --use-sips`

## Create App
 1. Install py2app: `python3 -m pip install py2app`
 2. Create the setup script by running the py2applet utility that comes bundled with py2app: `/Users/cstout16/Library/Python/3.9/bin/py2applet --make-setup flashcards.py`
 3. Modify the setup.py script to include `'iconfile':'paau2_image.icns'` in the `OPTIONS` variable.
 4. Create the app in alias mode: `python3 setup.py py2app -A`
 5. The app is created at `dist/flashcards.app`
