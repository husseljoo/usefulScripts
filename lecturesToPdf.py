import os


def main():
    path = os.getcwd()
    # path = "/home/husseljo/uni/microprocessors/test_lectures"
    print(path)
    all_files = os.listdir()
    target_files = list(filter(lambda x: x.endswith("pptx"), all_files))

    for file in target_files:
        new_file = file.replace(" ", "").partition("_")[0].lower()
        number = new_file[-2:]
        if number[0].isnumeric():
            new_file = f"lecture_{number}.pdf"
        else:
            new_file = f"lecture_{number[1]}.pdf"
        os.rename(file, new_file)
        os.system(f"soffice --headless --convert-to pdf {new_file}")


if __name__ == "__main__":
    main()
