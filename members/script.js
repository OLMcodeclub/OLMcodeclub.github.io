function listMembers() {
  var members = ["Paco0409", "Mimi24798", "Kaker", "Potato081", "Crazydann", "Pulif", "Biancaio29", "PurpleNinja3", "GrandDiamond67"];
  var counter = 0;
  while (counter < members.length) {
    document.getElementById("memberList").innerHTML = document.getElementById("memberList").innerHTML + "<br /><a href='https://scratch.mit.edu/users/" + members[counter] + "' target='_blank'>" + members[counter] + "</a>";
    counter = counter + 1;
  }
}
