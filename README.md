# 🟢 Aurora Speech Extractor

**Version:** 2.0  
**Author:** Pynexor Ltd.  
**License:** MIT License

## ✅ What is Aurora Speech Extractor?

**Aurora Speech Extractor** is a modern, feature-rich desktop application that converts speech from audio and video files into written text using advanced AI technology. Built with a beautiful, intuitive interface, it supports multiple output formats, real-time progress tracking, and drag-and-drop functionality.

### 🌟 Key Features

- **🎯 Advanced AI Transcription** - Powered by OpenAI's Whisper model for high-accuracy speech recognition
- **📁 Multiple Input Formats** - Supports audio (MP3, WAV, M4A) and video (MP4, MKV, AVI) files
- **📄 Multiple Output Formats** - Export as SRT subtitles, plain text, PDF, or Word documents
- **🖱️ Drag & Drop Interface** - Simply drag files onto the application window
- **📊 Real-time Progress Tracking** - Dynamic progress bar with status updates and elapsed time
- **🎨 Modern UI Design** - Clean, professional interface with responsive design
- **⚡ Fast Processing** - Optimized for quick transcription with background processing

---

## 🛠️ System Requirements

### Minimum Requirements
- **Operating System:** Windows 10 or higher
- **RAM:** 4GB (8GB recommended)
- **Storage:** 2GB free space
- **Internet Connection:** Required for initial model download (one-time)

### Recommended Requirements
- **RAM:** 8GB or higher
- **Storage:** 5GB free space
- **CPU:** Multi-core processor
- **GPU:** CUDA-compatible GPU (optional, for faster processing)

### Supported File Formats

#### Input Formats
- **Audio:** `.mp3`, `.wav`, `.m4a`
- **Video:** `.mp4`, `.mkv`, `.avi`

#### Output Formats
- **SRT (Subtitles)** - SubRip subtitle format with timestamps
- **TXT (Plain Text)** - Simple text file with transcribed content
- **PDF** - Professional document with formatted text
- **Word (.docx)** - Editable Microsoft Word document

---

## 📦 Installation

### Option 1: Standalone Executable (Recommended)
1. Download `Aurora_Speech_Extractor.exe`
2. Place it in any folder (no installation required)
3. Ensure `icon.ico` and `logo.png` are in the same folder (if not bundled)
4. Double-click to run

### Option 2: Python Development Setup
1. Clone or download the source code
2. Install Python 3.10 or higher
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run the application:
   ```bash
   python aurora.py
   ```

### Dependencies
The application requires the following Python packages:
- `openai-whisper` - AI transcription engine
- `moviepy` - Video processing
- `tkinterdnd2` - Drag and drop functionality
- `Pillow` - Image processing
- `reportlab` - PDF export
- `python-docx` - Word document export
- `torch` - Machine learning framework

---

## 🚀 How to Use

### 🔹 Step 1: Launch the Application
- Double-click `Aurora_Speech_Extractor.exe`
- The application opens with a modern interface featuring the Aurora logo
- The main window displays the drag-and-drop area and format selection

### 🔹 Step 2: Select Output Format
- Choose your desired output format from the dropdown menu:
  - **SRT (Subtitles)** - For video subtitles with timestamps
  - **TXT (Plain Text)** - For simple text documents
  - **PDF** - For professional documents
  - **Word (.docx)** - For editable documents

### 🔹 Step 3: Add Your File
You can add files in two ways:

#### Method A: Drag and Drop
1. Drag your audio/video file from File Explorer
2. Drop it onto the application window
3. The file will be automatically processed

#### Method B: File Browser
1. Click the **"📂 Select File"** button
2. Browse to your audio/video file
3. Click **"Open"** to start processing

### 🔹 Step 4: Monitor Progress
During processing, you'll see:
- **Real-time progress bar** showing completion percentage
- **Status messages** indicating current operation
- **Elapsed time** counter
- **File information** including name and size

### 🔹 Step 5: Save Results
- When processing completes, a save dialog will appear
- Choose your desired location and filename
- The file will be saved in your selected format
- A success message will confirm the operation

---

## 🎯 Output Format Details

### SRT (Subtitles)
- **Best for:** Video subtitles, presentations, interviews
- **Features:** Timestamps for each segment, numbered entries
- **Example:**
  ```
  1
  00:00:01,000 --> 00:00:04,000
  Hello, welcome to our presentation.
  
  2
  00:00:04,000 --> 00:00:07,000
  Today we'll discuss the new features.
  ```

### TXT (Plain Text)
- **Best for:** Simple text documents, notes, transcripts
- **Features:** Clean text without timestamps
- **Example:**
  ```
  Hello, welcome to our presentation. Today we'll discuss the new features.
  ```

### PDF
- **Best for:** Professional documents, reports, formal transcripts
- **Features:** Formatted document with title and structured content
- **Includes:** Professional layout with proper spacing and formatting

### Word (.docx)
- **Best for:** Editable documents, reports, collaborative work
- **Features:** Fully editable document with proper formatting
- **Includes:** Title, structured paragraphs, ready for editing

---

## 💡 Tips for Best Results

### Audio Quality
- **Use clear audio** with minimal background noise
- **Avoid echo** and reverberation
- **Ensure good microphone quality** for recordings
- **Keep consistent volume levels**

### File Preparation
- **Trim unnecessary silence** from the beginning and end
- **Use appropriate file formats** (MP3 for audio, MP4 for video)
- **Keep file sizes reasonable** (under 100MB for optimal performance)
- **Ensure stable audio/video playback** before processing

### Processing Optimization
- **Close other applications** to free up system resources
- **Use SSD storage** for faster file access
- **Ensure adequate RAM** for large files
- **Consider file length** - longer files take more time

---

## ❓ Troubleshooting

### Common Issues

#### Application Won't Start
- **Solution:** Check if antivirus is blocking the executable
- **Alternative:** Run as administrator
- **Check:** Ensure all required files are in the same folder

#### Import Errors
- **Error:** `ModuleNotFoundError: No module named 'tkinterdnd2'`
- **Solution:** Install missing dependencies: `pip install tkinterdnd2`
- **Error:** `ModuleNotFoundError: No module named 'whisper'`
- **Solution:** Install Whisper: `pip install openai-whisper`

#### Processing Issues
- **Problem:** Progress bar stuck at 0%
- **Solution:** Check file format compatibility
- **Problem:** No output generated
- **Solution:** Try a different audio file with clearer speech

#### Format Export Issues
- **PDF export fails:** Install reportlab: `pip install reportlab`
- **Word export fails:** Install python-docx: `pip install python-docx`

### Performance Issues
- **Slow processing:** Close other applications
- **Memory errors:** Use smaller files or increase RAM
- **GPU not detected:** Install CUDA drivers for GPU acceleration

---

## 🔧 Technical Details

### Architecture
- **Frontend:** Tkinter with custom styling
- **Backend:** Python with multi-threading
- **AI Engine:** OpenAI Whisper (base model)
- **Video Processing:** MoviePy library
- **Document Generation:** ReportLab (PDF), python-docx (Word)

### Processing Pipeline
1. **File Validation** - Check format and size
2. **Audio Extraction** - Extract audio from video files
3. **AI Transcription** - Process audio with Whisper model
4. **Format Conversion** - Convert to selected output format
5. **File Export** - Save to user-specified location

### Performance Characteristics
- **Processing Speed:** ~1-2x real-time (depends on hardware)
- **Memory Usage:** 2-4GB RAM during processing
- **Storage:** Temporary files created during processing
- **Accuracy:** High accuracy for clear speech, moderate for noisy audio

---

## 📜 License

Aurora Speech Extractor is provided under the **MIT License**.

### License Terms
- **Use:** Free for personal and commercial use
- **Modify:** You can modify the source code
- **Distribute:** You can distribute modified versions
- **Attribution:** Credit to Pynexor Ltd. is appreciated

### Copyright
© 2025 Pynexor Ltd. All rights reserved.

---

## 🤝 Support

For support, bug reports, or feature requests:
- **Email:** support@pynexor.com
- **GitHub:** Create an issue in the repository
- **Documentation:** Check this README for common solutions

---

## 🔄 Version History

### Version 2.0 (Current)
- ✅ Multiple output formats (SRT, TXT, PDF, Word)
- ✅ Modern UI with drag-and-drop
- ✅ Real-time progress tracking
- ✅ Enhanced error handling
- ✅ Professional document generation

### Version 1.0
- ✅ Basic audio/video transcription
- ✅ Simple text output
- ✅ Basic GUI interface

---

*Built with ❤️ by Pynexor Ltd.*

