function transform(line) {
  var values = line.split(",");
  var obj = new Object();
  obj.player_no = values[0];
  obj.name = values[1];
  obj.att_won = values[2];
  obj.att_att = values[3];
  obj.block_won = values[4];
  obj.block_att = values[5];
  obj.serv_won = values[6];
  obj.serv_att = values[7];
  obj.dig_exc = values[8];
  obj.dig_att = values[9];
  obj.rec_exc = values[10];
  obj.rec_att = values[11];
  obj.set_exc = values[12];
  obj.set_att = values[13];
  obj.match_no = values[14];
  obj.match_title = values[15];
  var jsonString = JSON.stringify(obj);
  return jsonString;
}
