  var token = "5278477646:AAFMg-qeonrALs4aYe2A2uSYj41qVcOzyGA";
  var SheetID_ibu = "1zHLgXS0T4Twg5Um8gX609xTYWMTXy8errAgOQkOZ06g";
  var SheetID_kerjaanhariz = "1Mdp0AFAC0j31O37sjGo1Vh5Bkotky241MT0FmD4GI4c";

  function doPost(e) {
    var stringJson = e.postData.getDataAsString();
    var updates = JSON.parse(stringJson);
    // sendText(updates.message.chat.id,updates);
    // Logger.log(updates.message.text);
  
      if(updates.message.text.split(" ")[0]=="/listkerja"){
        if(updates.message.text.split(" ")[1]==="idle"){
          sendText(updates.message.chat.id,CariBarangDariIDSheet("idle")); 
          }
        else if(updates.message.text.split(" ")[1]==="ongoing"){
          sendText(updates.message.chat.id,CariBarangDariIDSheet("ongoing")); 
        }
        else if(updates.message.text.split(" ")[1]==="done"){
          sendText(updates.message.chat.id,CariBarangDariIDSheet("done")); 
        }
        else {
          sendText(updates.message.chat.id,"Please add status:\n Example: <pre>/listkerja idle</pre> | <pre>/listkerja ongoing</pre> | <pre>/listkerja done</pre>");
        }
      }

      else if(updates.message.text.split(" ")[0]=="/updatekerja"){
        if(updates.message.text.split(" ")[1]){
          if(updates.message.text.split(" ")[2]==="done"){
            sendText(updates.message.chat.id,UpdateKerjaan(updates,"done"));
          }
          else if(updates.message.text.split(" ")[2]==="idle"){
            sendText(updates.message.chat.id,UpdateKerjaan(updates,"idle"));
          }
          else if(updates.message.text.split(" ")[2]==="ongoing"){
            sendText(updates.message.chat.id,UpdateKerjaan(updates,"ongoing"));
          }
          else {
            sendText(updates.message.chat.id,"Please add work status: Example <pre>/updatekerja 3 done</pre> | <pre>/updatekerja 3 idle</pre> | <pre>/updatekerja 3 ongoing</pre>");
          }
          }
        else {
          sendText(updates.message.chat.id,"Please add id:\n Example: <pre>/updatekerja 3 done</pre> | <pre>/updatekerja 4 idle</pre>");
        }
      }
      else if(updates.message.text=="/ibusatu"){
        sendText(updates.message.chat.id,Result(updates));
      }
      else if(updates.message.text.split(" ")[0]=="/ibumakan"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates, "makanan"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibumakan 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibubayi"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates, "bayi"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibubayi 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibuibu"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"ibu"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibuibu 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibumart"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"mart"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibumart 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibugalon"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates, "galon"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibugalon 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibusayur"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"sayur"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibusayur 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibusedekah"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"sedekah"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibusedekah 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibulistrik"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"listrik"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibulistrik 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibupdam"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"air"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibupdam 50000</pre>")
        }
      }
      else if(updates.message.text.split(" ")[0]=="/ibukebkea"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates,"kk"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibukebkea 50000</pre>")
        }
      }

      else if(updates.message.text.split(" ")[0]=="/ibuinternet"){
        if(updates.message.text.split(" ")[1]){
          sendText(updates.message.chat.id,Add(updates, "internet"));
          }
        else {
          sendText(updates.message.chat.id,"Please add amount: Example <pre>/ibuinternet 50000</pre>")
        }
      }

      else {
        sendText(updates.message.chat.id,"Perintah salah");
      }
  }

  // Main Functions
  function sendText(chatid,text,replymarkup){
    var data = {
        method: "post",
        payload: {
          method: "sendMessage",
          chat_id: String(chatid),
          text: text,
          parse_mode: "HTML",
          reply_markup: JSON.stringify(replymarkup)
        }
      };
      UrlFetchApp.fetch('https://api.telegram.org/bot' + token + '/', data);
    }

  function AmbilSheet(range,sheet_ID){
    var rangeName = range;
    var rows = Sheets.Spreadsheets.Values.get(sheet_ID, rangeName).values;
    return rows;
  }

  function UpdateSheet(value, range, sheet_ID){
    var rangeName = range;
    var value = value
    var result = Sheets.Spreadsheets.Values.update(
      {values:[[value]]},
      sheet_ID,rangeName,
      {valueInputOption: "USER_ENTERED"}
    );
    return result;
  }

  function text_formatting(word, panjang){
    for (var start = word.length; start < panjang; start ++){
      word +=" ";
    }
    return word;
  }

  // Hariz PSN

  function CariBarangDariIDSheet(status){
    var range_val = 'Sheet1!A2:D';
    var dataBarang = AmbilSheet(range_val, SheetID_kerjaanhariz); 
    var result = "";
    for (var row = 0; row < dataBarang.length; row++) {
      if (dataBarang[row][3]===status){
        var result = result + "ID : "+row+"\n"+
              "Nama Kerjaan : " + dataBarang[row][0] + "\n" +
              "Deskripsi :\n" + dataBarang[row][1] + "\n" + 
              "Prioritas  : " + dataBarang[row][2] + "\n"+
              "Status : " + dataBarang[row][3]+ "\n\n";
      }
    }
    return result;
  }

  function UpdateKerjaan(debug,status){
    var id = debug.message.text.split(" ")[1];
    var range_update = 'Sheet1!D'
    var cell = range_update+(parseInt(id)+2);
    UpdateSheet(status,cell,SheetID_kerjaanhariz);

    var range_val = 'Sheet1!A2:D';
    var dataBarang = AmbilSheet(range_val, SheetID_kerjaanhariz); 
    var result = "New Result Shown Below!\n";
    for (var row = 0; row < dataBarang.length; row++) {
      if (row===parseInt(id)){
        var result = result + "Nama Kerjaan : " + dataBarang[row][0] + "\n" +
              "Deskripsi :\n" + dataBarang[row][1] + "\n" + 
              "Prioritas  : " + dataBarang[row][2] + "\n"+
              "Status : " + dataBarang[row][3]+ "\n\n";
      }
    }
    return result;
  }

  // Ibu satu
  function Result(debug=""){
    var nilai_extra_short = AmbilSheet('Sheet2!C1:M1', SheetID_ibu);
    var nama_kolom = AmbilSheet('Sheet2!C4:M4',SheetID_ibu);
    var result = "<pre>+----------+--------------+\n| Kategori | Nominal Sisa |\n+----------+--------------+\n";
    for (var col = 0; col < nilai_extra_short[0].length; col++) {
      var result = result + "|" +text_formatting(nama_kolom[0][col],10)+ "|" + text_formatting(nilai_extra_short[0][col],14) + "|\n";
    }
    result += "+----------+--------------+</pre>\n";
    var total_sisa = AmbilSheet('Sheet2!N1', SheetID_ibu);
    result += "<b>Sisa uang belanjaan "+total_sisa+"</b>";
    return result;
  }

  // Ibu makan
  function Add(debug="", kolom=""){

    var update_value = debug.message.text.split(" ")[1];

    var range_val = 'Sheet2!B7:B37';
    var dataTanggal = AmbilSheet(range_val, SheetID_ibu);
    var dataCell = AmbilSheet(range_val, SheetID_ibu);;

    // modified month length
    var today = new Date();
    var month = today.getMonth()+1;
    month = month.toString();
    if (month.length===1){
      month = "0"+month;
    }
    var date = today.getDate()+"/"+month+"/"+today.getFullYear();

    var nama_kolom = "";

    if (kolom === "makanan"){
      range_kolom = "Sheet2!C";
    } else if (kolom === "bayi") {
      range_kolom = "Sheet2!D";
    } else if (kolom === "ibu") {
      range_kolom = "Sheet2!E";
    } else if (kolom === "mart") {
      range_kolom = "Sheet2!F";
    } else if (kolom === "galon") {
      range_kolom = "Sheet2!G";
    } else if (kolom === "sayur") {
      range_kolom = "Sheet2!H";
    } else if (kolom === "sedekah") {
      range_kolom = "Sheet2!I";
    } else if (kolom === "listrik") {
      range_kolom = "Sheet2!J";
    } else if (kolom === "air") {
      range_kolom = "Sheet2!K";
    } else if (kolom === "kk") {
      range_kolom = "Sheet2!L";
    } else if (kolom === "internet") {
      range_kolom = "Sheet2!M";
    }

    var range_update = "";

    for (var row = 0; row < dataTanggal.length; row++){
      if (dataTanggal[row][0]==date){
        range_update = range_kolom+(row+7);
        dataCell = AmbilSheet(range_update, SheetID_ibu);
        if (dataCell){
          var values = "="+dataCell[0][0].substr(2).replace(",","")+"+"+update_value;
          var range_update = 'Sheet2!C'+(row+7)+":C"+(row+7); 
          var result = UpdateSheet(values, range_update, SheetID_ibu);
          var today_value = AmbilSheet(range_update, SheetID_ibu);
          return "Uang sebesar Rp." + update_value  + "telah tersimpan. Total pengeluaran hari ini " + today_value;
        }
        else {
          var values = "="+update_value;
          var range_update = 'Sheet2!C'+(row+7)+":C"+(row+7);
          var result = UpdateSheet(values, range_update, SheetID_ibu);
          var today_value = AmbilSheet(range_update, SheetID_ibu);
          return "Uang sebesar Rp." + update_value  + "telah tersimpan. Total pengeluaran hari ini " + today_value;
        }
      }
    }
    return "Date not found!";
  }

