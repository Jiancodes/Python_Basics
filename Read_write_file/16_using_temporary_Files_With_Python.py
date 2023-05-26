# 用Python使用临时文件
import tempfile

# Create a temporary file
temp_file = tempfile.TemporaryFile()

# Write to a temporary file
temp_file.write(b'Save the date: 070420')
temp_file.seek(0)

# Read the temporary file
print(temp_file.read())

# Close the temporary file
temp_file.close()

### 