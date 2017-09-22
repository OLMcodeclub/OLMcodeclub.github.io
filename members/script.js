function listMembers() {
  var members = ["mrawesomescratcher", "flamingfireball64"];
  var counter = 0;
  while (counter < members.length) {
    document.getElementById("memberList").innerHTML = document.getElementById("memberList").innerHTML + "<br /><a href='https://scratch.mit.edu/users/" + members[counter] + "' target='_blank'>" + members[counter] + "</a>";
    counter = counter + 1;
  }
}
