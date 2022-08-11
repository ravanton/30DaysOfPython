# Get user input
filename = input("File name: ").strip().lower()

# If .gif or .png or .jpg or .jpeg, print "image/type"
if ".gif" or ".png" or ".jpg" or ".jpeg" in filename:
    print("image/gif")
elif ".png"  in filename:
    print("image/png")
elif ".jpg" or ".jpeg" in filename:
    print("image/jpeg")

# If .pdf or .zip , print "application/type"
elif ".pdf" in filename:
    print("application/pdf")
elif ".zip" in filename:
    print("application/zip")
# If txt, print "text/type"
elif ".txt" in filename:
    print("text/type")

#Otherwise, print "application/octec-stream"
else:
    print("application/octec-stream")
