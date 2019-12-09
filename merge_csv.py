import pandas as pd
import argparse
import os


def main():
    parser = argparse.ArgumentParser(description="Merge ADNI csv files.")
    parser.add_argument("input_dir", help="Path to the directory containing the input csv files.")
    parser.add_argument("-o", "--output", default="./ADNI_MERGE.csv", help="Path for output file.")
    parser.add_argument("-p", "--phase", default="all", help="Phase to keep, default all.")
    parser.add_argument("-v", "--viscode", default="all", help="VISCODE to keep, default all.")

    args = parser.parse_args()

    ### columns common to all files to use as index ###
    index = ["RID", "VISCODE"]  # , "EXAMDATE"]

    ### Loading csv files ###
    UCD_ADNI1_WMH = pd.read_csv(os.path.join(args.input_dir, "UCD_ADNI1_WMH.csv"), index_col=index)
    PTDEMOG = pd.read_csv(os.path.join(args.input_dir, "PTDEMOG.csv"), index_col=index)
    MRI_INFARCTS_11_16_15 = pd.read_csv(os.path.join(args.input_dir, "MRI_INFARCTS_11_16_15.csv"), index_col=index)
    VITALS = pd.read_csv(os.path.join(args.input_dir, "VITALS.csv"), index_col=index)

    ### Columns to keep: ###
    columns_UCD_ADNI1_WMH = ["WHITMATHYP"]
    columns_PTDEMOG = ["Phase", "PTGENDER", "PTDOBMM", "PTDOBYY"]
    columns_MRI_INFARCTS_11_16_15 = ["INFARCT_NUMBER",]
    columns_VITALS = ["VSBPSYS", "VSBPDIA", "VSPULSE", "VSWEIGHT", "VSHEIGHT"]

    ### getting set of all (ADNI1, RID, VISCODE2) ###
    indices = UCD_ADNI1_WMH.index
    indices = indices.append(MRI_INFARCTS_11_16_15.index)
    indices = indices.append(PTDEMOG.index)
    indices = indices.append(VITALS.index)

    ### creating output ###
    output = pd.DataFrame(index=indices.unique())
    # output.to_csv("./test_indices.csv")
    output = output.join(UCD_ADNI1_WMH[columns_UCD_ADNI1_WMH], on=index)
    output = output.join(PTDEMOG[columns_PTDEMOG], on=index)
    output = output.join(MRI_INFARCTS_11_16_15[columns_MRI_INFARCTS_11_16_15], on=index)
    output = output.join(VITALS[columns_VITALS], on=index)

    ### filtering lines ###
    if args.phase != "all":
        output = output.query("Phase=='{}'".format(args.phase))
    if args.viscode != "all":
        output = output.query("VISCODE=='{}'".format(args.viscode))

    output.to_csv(args.output)


if __name__ == "__main__":
    main()
