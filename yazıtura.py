{
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "background_save": true,
          "base_uri": "https://localhost:8080/"
        },
        "id": "_BfgxQsXaAS2",
        "outputId": "388b3315-de28-4aa0-8558-2d7a32c456d9"
      },
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Yukarı...\n",
            "Aşağı...\n"
          ]
        }
      ],
      "source": [
        "import random\n",
        "while True:\n",
        "  s=random.randint(1,100)\n",
        "  deneme=0\n",
        "  while True:\n",
        "    t=int(input(\"Tahmin:\"))\n",
        "    deneme +=1\n",
        "    if t<s:\n",
        "      print(\"Yukarı...\")\n",
        "    elif   t>s:\n",
        "        print(\"Aşağı...\")\n",
        "    elif t==s:\n",
        "          print(f\"Tebrikler {deneme}  denemede bildiniz\")\n",
        "          break\n",
        "          a=input(\"Devam mı? e/h:\")\n",
        "          if a in \"hH\":\n",
        "            break"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}