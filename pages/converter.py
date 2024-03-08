import streamlit as st
import cv2
from moviepy.editor import VideoFileClip, AudioFileClip
import os
import numpy as np
from PIL import Image


st.title("File Converter")
st.write("This app allows you to convert files from one format to another.")


# Function to convert .jpg to .png
def jpg_to_png():
    # Prompt user to select a file
    jpg_file = st.file_uploader("Select a .jpg or .jpeg file", type=[
                                "jpg", "jpeg"], key="jpg_to_png")

    if jpg_file is not None:
        # Convert .jpg to .png
        img_array = np.frombuffer(jpg_file.read(), np.uint8)
        img = cv2.imdecode(img_array, cv2.IMREAD_COLOR)
        png_data = cv2.imencode('.png', img)[1].tobytes()

        # Convert to PIL Image
        pil_img = Image.fromarray(img)

        # Display the converted image
        st.image(pil_img, caption="Converted .png Image",
                 use_column_width=True)

        # Offer download link for the converted file
        st.download_button(label="Download .png", data=png_data,
                           file_name="converted_image.png", mime="image/png")

# Function to convert .png to .jpg


def png_to_jpg():
    # Prompt user to select a file
    png_file = st.file_uploader("Select a .png file", type=[
                                "png"], key="png_to_jpg")

    if png_file is not None:
        # Convert .png to .jpg
        img = cv2.imdecode(np.frombuffer(
            png_file.read(), np.uint8), cv2.IMREAD_COLOR)
        # Convert image to RGB format (Streamlit uses RGB)
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        # Convert image to bytes
        jpg_bytes = cv2.imencode('.jpg', img_rgb)[1].tobytes()

        # Display the converted image
        st.image(img_rgb, caption="Converted .jpg Image",
                 use_column_width=True)

        # Offer download link for the converted file
        st.download_button(label="Download .jpg", data=jpg_bytes,
                           file_name="converted_image.jpg", mime="image/jpeg")


# Function to convert .mkv to .mp4


def mkv_to_mp4():
    # Prompt user to select a file
    mkv_file = st.file_uploader("Select a .mkv file", type=[
                                "mkv"], key="mkv_to_mp4")

    if mkv_file is not None:
        # Convert .mkv to .mp4
        with st.spinner("Converting..."):
            video_clip = VideoFileClip(mkv_file)
            video_clip.write_videofile(
                "converted_video.mp4", codec='libx264', audio_codec='aac')

        # Display message about conversion completion
        st.success("Conversion completed!")

        # Offer download link for the converted file
        st.download_button(label="Download .mp4", data="converted_video.mp4",
                           file_name="converted_video.mp4", mime="video/mp4")

# Function to convert .mp4 to .mkv


def mp4_to_mkv():
    # Prompt user to select a file
    mp4_file = st.file_uploader("Select a .mp4 file", type=[
                                "mp4"], key="mp4_to_mkv")

    if mp4_file is not None:
        # Convert .mp4 to .mkv
        with st.spinner("Converting..."):
            video_clip = VideoFileClip(mp4_file)
            video_clip.write_videofile(
                "converted_video.mkv", codec='libx264', audio_codec='aac')

        # Display message about conversion completion
        st.success("Conversion completed!")

        # Offer download link for the converted file
        st.download_button(label="Download .mkv", data="converted_video.mkv",
                           file_name="converted_video.mkv", mime="video/x-matroska")

# Function to convert .mp4 to .avi


def mp4_to_avi():
    # Prompt user to select a file
    mp4_file = st.file_uploader("Select a .mp4 file", type=[
                                "mp4"], key="mp4_to_avi")

    if mp4_file is not None:
        # Convert .mp4 to .avi
        with st.spinner("Converting..."):
            video_clip = VideoFileClip(mp4_file)
            video_clip.write_videofile(
                "converted_video.avi", codec='rawvideo', audio_codec='pcm_s16le')

        # Display message about conversion completion
        st.success("Conversion completed!")

        # Offer download link for the converted file
        st.download_button(label="Download .avi", data="converted_video.avi",
                           file_name="converted_video.avi", mime="video/x-msvideo")

# Function to convert .avi to .mp4


def avi_to_mp4():
    # Prompt user to select a file
    avi_file = st.file_uploader("Select a .avi file", type=[
                                "avi"], key="avi_to_mp4")

    if avi_file is not None:
        # Convert .avi to .mp4
        with st.spinner("Converting..."):
            video_clip = VideoFileClip(avi_file)
            video_clip.write_videofile(
                "converted_video.mp4", codec='libx264', audio_codec='aac')

        # Display message about conversion completion
        st.success("Conversion completed!")

        # Offer download link for the converted file
        st.download_button(label="Download .mp4", data="converted_video.mp4",
                           file_name="converted_video.mp4", mime="video/mp4")


def mov_to_mp4():
    mov_file = st.file_uploader("Select a .mov file", type=[
                                "mov"], key="mov_to_mp4")

    if mov_file is not None:
        clip = VideoFileClip(mov_file)
        mov_name = os.path.basename(mov_file.name)
        mov_name_without_ext, _ = os.path.splitext(mov_name)
        i = 1
        while True:
            file_name = 'modified{}_{}.mp4'.format(i, mov_name_without_ext)
            file_path = os.path.join('Downloads', file_name)
            if not os.path.exists(file_path):
                clip.write_videofile(
                    file_path, codec='libx264', audio_codec='aac')
                break
            i += 1

        st.success("Conversion complete!")


def mp4_to_mov():
    mp4_file = st.file_uploader("Select a .mp4 file", type=[
                                "mp4"], key="mp4_to_mov")

    if mp4_file is not None:
        # Save the uploaded file locally
        with open("temp.mp4", "wb") as f:
            f.write(mp4_file.read())

        # Read the local file and create VideoFileClip
        clip = VideoFileClip("temp.mp4")

        mp4_name = os.path.basename(mp4_file.name)
        mp4_name_without_ext, _ = os.path.splitext(mp4_name)
        i = 1
        while True:
            file_name = f'modified{i}_{mp4_name_without_ext}.mov'
            file_path = os.path.join('Downloads', file_name)
            try:
                clip.write_videofile(
                    file_path, codec='libx264', audio_codec='aac')
            except OSError as e:
                # Handle the case where the directory doesn't exist
                os.makedirs('Downloads', exist_ok=True)
                clip.write_videofile(
                    file_path, codec='libx264', audio_codec='aac')
            except Exception as e:
                st.error(f"Error: {e}")
                break
            else:
                st.success("Conversion complete!")
                break
            i += 1


def main():
    conversion_choice = st.selectbox("Select conversion type", [
                                     "JPEG to PNG", "PNG to JPEG", "MOV to MP4", "MP4 to MOV", "AVI to MP4", ])

    if conversion_choice == "JPEG to PNG":
        jpg_to_png()
    elif conversion_choice == "PNG to JPEG":
        png_to_jpg()
    elif conversion_choice == "MOV to MP4":
        mov_to_mp4()
    elif conversion_choice == "MP4 to MOV":
        mp4_to_mov()
    elif conversion_choice == "AVI to MP4":
        avi_to_mp4()


if __name__ == "__main__":
    main()
