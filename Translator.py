{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPzpVn0WKT3zMmi3SEFDNy6"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "PGR0g7j5YaH9"
      },
      "outputs": [],
      "source": [
        "import tkinter as tk\n",
        "from tkinter import ttk\n",
        "from tkinter import scrolledtext\n",
        "from gtts import gTTS\n",
        "from googletrans import Translator\n",
        "from playsound import playsound\n",
        "\n",
        "# List of supported languages and their corresponding language codes\n",
        "languages = {\n",
        "    'English': 'en',\n",
        "    'French': 'fr',\n",
        "    'German': 'de',\n",
        "    'Spanish': 'es',\n",
        "    'Italian': 'it',\n",
        "    'Japanese': 'ja',\n",
        "    'Korean': 'ko',\n",
        "    'Chinese': 'zh-cn',\n",
        "    'Russian': 'ru',\n",
        "    'Arabic': 'ar',\n",
        "}\n",
        "\n",
        "\n",
        "def translate_and_speak():\n",
        "    text = text_entry.get(\"1.0\", \"end-1c\")  # Get text from the scrolled text widget\n",
        "    selected_language = language_var.get()\n",
        "\n",
        "    if selected_language in languages:\n",
        "        target_language = languages[selected_language]\n",
        "        translator = Translator()\n",
        "        translated_text = translator.translate(text, dest=target_language).text\n",
        "\n",
        "        tts = gTTS(translated_text, lang=target_language)\n",
        "        tts.save(\"output.mp3\")\n",
        "        playsound(\"output.mp3\")\n",
        "    else:\n",
        "        output_label.config(text=\"Selected language is not supported!\")\n",
        "\n",
        "\n",
        "# Create the main window\n",
        "root = tk.Tk()\n",
        "root.title(\"Text to Speech Translator\")\n",
        "root.geometry(\"400x400\")\n",
        "root.configure(bg=\"green\")\n",
        "\n",
        "# Label\n",
        "label = ttk.Label(root, text=\"Enter text:\")\n",
        "label.pack(pady=10)\n",
        "\n",
        "# Scrolled Text Entry\n",
        "text_entry = scrolledtext.ScrolledText(root, width=30, height=10)\n",
        "text_entry.pack()\n",
        "\n",
        "# Language Selection\n",
        "language_var = tk.StringVar()\n",
        "language_var.set('English')  # Default language\n",
        "language_label = ttk.Label(root, text=\"Select Language:\")\n",
        "language_label.pack()\n",
        "language_menu = ttk.OptionMenu(root, language_var, *languages.keys())\n",
        "language_menu.pack()\n",
        "\n",
        "# Translate and Speak Button\n",
        "convert_button = ttk.Button(root, text=\"Translate and Speak\", command=translate_and_speak)\n",
        "convert_button.pack(pady=10)\n",
        "\n",
        "# Output Label\n",
        "output_label = ttk.Label(root, text=\"\")\n",
        "output_label.pack()\n",
        "\n",
        "# Run the GUI main loop\n",
        "root.mainloop()"
      ]
    }
  ]
}