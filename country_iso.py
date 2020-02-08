import csv


def extract_country_iso_code(in_file, out_file):

    with open(in_file, "r") as csvinput:
        with open(out_file, "w") as csvoutput:
            writer = csv.writer(csvoutput, lineterminator="\n")
            reader = csv.reader(csvinput)

            all = []
            row = next(reader)

            for row in reader:
                row.append(row[1] + ".jpg")
                all.append(row)

            writer.writerows(all)


extract_country_iso_code(
    "./resources/data/country_iso_codes.csv", "./resources/data/country_iso_images.csv"
)

