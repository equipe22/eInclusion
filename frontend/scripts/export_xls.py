"""
script creant un fichier xls a partir des donnees Einclusion
input : dic_data => {var1 ...


"""
from io import BytesIO
import numpy as np
import pandas as pd

def export_data_to_excel(data):

    df_1 = pd.DataFrame.from_dict(data)

    # create an output stream
    output = BytesIO()
    writer = pd.ExcelWriter(output, engine='xlsxwriter')

    # taken from the original question
    df_1.to_excel(writer, startrow=0, merge_cells=False, sheet_name="Sheet_1", index=False)
    workbook = writer.book
    worksheet = writer.sheets["Sheet_1"]

    format = workbook.add_format()
    format.set_bg_color('#eeeeee')
    worksheet.set_column(0, 9, 28)

    # the writer has done its job
    writer.close()

    # go back to the beginning of the stream
    output.seek(0)

    # finally return the file
    return output
