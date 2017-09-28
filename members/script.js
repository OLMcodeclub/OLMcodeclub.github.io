function listMembers() {
  var members = ["Paco0409", "Mimi24798", "Kaker", "Potato081", "Crazydann", "Pulif", "Biancaio29", "PurpleNinja3", "GrandDiamond67", "JohnSiena20", "ironman226", "ironman225", "PurpleNinja17", "pingupokemon", "monkey1408", "chickenfan2111", "adka10", "cakebin", "superfish999", "policeee", "Pscratch2610", "lolscratch2006"];
  var counter = 0;
  while (counter < members.length) {
    document.getElementById("memberList").innerHTML = document.getElementById("memberList").innerHTML + "<br /><a href='https://scratch.mit.edu/users/" + members[counter] + "' target='_blank'>" + members[counter] + "</a>";
    counter = counter + 1;
  }
}
