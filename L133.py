#Emily Nixon and Katie O'Rourke
import dbm
db1 = dbm.open("Lab 13", "c")
db1["jogger.jpeg"]="a man running from his demons"
db1["swimmer.jpeg"]="a girl swimming away from a shark"
db1["volleyball.jpeg"] = "a team is using a cheese wheel as a volleyball"
db1["coders.jpeg"]="two coding students sob"
db1["gardener.jpeg"]="a gardener planting hot dogs"
db1["coders.jpeg"]="two coding students smiling at a computer"
db1["gardener.jpeg"]="a gardener planting a rose"
for item in db1:
    print(item,db1[item])
db1.close()
