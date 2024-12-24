

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/ffc25123-d914-4198-b225-2660c442c942" alt="Screenshot (49)">
</p>

# Python เงี้ยนโว้ยย เงี่ยนนน libary

This Python script allows you to interact with a class `NgianWoiiiNgian`, which provides several options to print text in Thai, English, Karaoke, or even generate audio. You can also open a YouTube link directly from the script.

## Requirements
- Python 3.x
- The required libraries will be automatically handled during execution. Ensure you have the required dependencies like `webbrowser`, `base64`, and others installed in your environment.

## Setup

1. Clone or download this repository.
2. Ensure you have Python installed on your system.

## Usage

### Import and Initialize the Class

```python
from NgianWoiiiNgian import NgianWoiiiNgian  # Import the class

# Create an instance of the class
app = NgianWoiiiNgian()
```

### Available Methods

- **Print Thai Text:**

  ```python
  app.NgianWoii_fun()  # This will print the Thai text
  ```

- **Print English Text:**

  ```python
  app.NgianWoii_fun(eng=True)  # This will print the English text
  ```

- **Print Karaoke Text:**

  ```python
  app.NgianWoii_fun(karaoke=True)  # This will print the Karaoke text
  ```

- **Open YouTube Link:**

  ```python
  app.NgianWoii_fun(open_link=True)  # This will open the YouTube link
  ```

  - The link that will be opened is: [https://youtu.be/cTr69ADnqH0?si=yu_wMThoSXtCaXuU](https://youtu.be/cTr69ADnqH0?si=yu_wMThoSXtCaXuU)

- **Loop Print (e.g., English Text 10 Times):**

  ```python
  app.NgianWoii_fun(eng=True, count=10)  # This will print the English text 10 times
  ```

- **Generate and Save Audio:**

  ```python
  app.NgianWoii_fun(audio=True)  # This will generate and save the audio once
  ```

- **Generate and Save Audio Multiple Times:**

  ```python
  app.NgianWoii_fun(audio=True, count_audio=3)  # This will generate and save the audio 3 times
  ```

### Example:

```python
from NgianWoiiiNgian import NgianWoiiiNgian

# Create an instance of the class
app = NgianWoiiiNgian()

# Print Thai text
app.NgianWoii_fun()

# Print English text
app.NgianWoii_fun(eng=True)

# Generate and save audio 3 times
app.NgianWoii_fun(audio=True, count_audio=3)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
