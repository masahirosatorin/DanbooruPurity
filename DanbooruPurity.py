from urllib.request import urlopen

laur = input("Remember to delete clean.txt and dirty.txt first.\nFile to read from: ")
my_file = open(laur, "r")
content = my_file.read()
sussy = content.split("\n")
print("Processing counts for all images...")
for item in sussy:
    sus = "https://danbooru.donmai.us/counts/posts.json?tags=" + item
    fetch = urlopen(sus)
    for shit in fetch:
        pog = str(shit)
        with open("total.txt", "a") as o:
            o.write(pog[21:-3] + "\n")
print("Processing counts for SFW images...")
for item in sussy:
    sus = "https://danbooru.donmai.us/counts/posts.json?tags=" + item + "+rating:s"
    fetch = urlopen(sus)
    for shit in fetch:
        pog = str(shit)
        with open("sfw.txt", "a") as o:
            o.write(pog[21:-3] + "\n")
print("Done!")
