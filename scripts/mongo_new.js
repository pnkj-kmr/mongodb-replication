cat > /tmp/mongo.js <<REALEND
conn = new Mongo();
db = conn.getDB("test_1");
var appobj = {"name":"App", "date": new Date()};
db.app__.save(appobj)
db.createUser(
{   user: "test",
    pwd: "Test@121$",
    roles:[{role: "dbOwner", db:"test_1"},],
    mechanisms: ["SCRAM-SHA-1"]
})
REALEND