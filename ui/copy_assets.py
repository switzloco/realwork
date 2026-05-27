import os
import shutil
import glob

brain_dir = r"C:\Users\nswitzer\.gemini\antigravity\brain\61b376da-3995-4b5e-b269-6c3f2a0d3b4c"
assets_dir = r"C:\Users\nswitzer\Antigrav Proj\realwork\ui\assets"

os.makedirs(assets_dir, exist_ok=True)

for png_file in glob.glob(os.path.join(brain_dir, "*.png")):
    shutil.copy(png_file, assets_dir)
    print(f"Copied {png_file} to {assets_dir}")
