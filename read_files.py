import numpy as np

# Read file with DUT1 = UT1 - UTC
file_dut1 = open("UTC.dat", "r")

jd_array1 = np.array(())
dut1_array = np.array(())

# Store julian day and respective DUT1 from file
for line in file_dut1:
    jd_array1 = np.append(jd_array1,float(line[7:15]))
    dut1_array = np.append(dut1_array,float(line[58:68]))

file_dut1.close()

# Convert from MJD to JD
jd_array1 = jd_array1 + 2400000.5

# Read file with DTAI = TAI - UTC
file_tai = open("TAI.dat", "r")

jd_array2 = np.array(())
dtai_array = np.array(())

# Store julian day and respective DTAI (= leap seconds) from file
for line in file_tai:
    jd_array2 = np.append(jd_array2,float(line[17:26]))
    dtai_array = np.append(dtai_array,float(line[38:48]))

file_tai.close()

# Write useful data in files
# DUT1:
file_dut1 = open("dut1.dat", "w")
file_dut1.write("Julian_date UT1-UTC\n")
for i in range(len(jd_array1)):
    file_dut1.write(str(jd_array1[i]) + " " + str(dut1_array[i]) + "\n")
file_dut1.close()

# DTAI:
file_dtai = open("dtai.dat", "w")
file_dtai.write("Julian_date Leap_seconds\n")
for i in range(len(jd_array2)):
    file_dtai.write(str(jd_array2[i]) + " " + str(dtai_array[i]) + "\n")
file_dtai.close()
