// Load words.txt to an Array
let words = new Array();
	$.get("words.txt", function(data){
			words = data.split("\n");
	});

// Load deffinition.txt into an array
let definition = new Array();
	$.get("definitions.txt", function(data){
			definition = data.split("\n");
	});

function shortQuery(term){
	terms = term.split(" ");
	buffer = "";
	for (i in terms){
		buffer += terms[i];
	}
	return buffer.toLowerCase();
}

// Function to spit out answers similar to what is searched
function search(textQ){
	let request = shortQuery(textQ);
	let index1 = [];
	let len = request.length;
	console.log(len);
	for (i in words){
		let x = words[i].slice(0, len);
		console.log(x);
		if (x == request){
			index1.push(i);}
	}
	return index1;
}

function copyText(index){
	let text1 = words[index] + " - " + definition[index];
	navigator.clipboard.writeText(text1);
}

// Main function, executed on button press
function main(){
	// Get word in the input box
	let term = $("#word_search").val();
	let indexR = 1;
	let template = words[indexR] + " - " + definition[indexR];
	let char_out = "";
	let search_results = search(term);
	console.log(search_results);
	//let char_out = "<div id='output1'><p style=\"font-family: 'Times New Roman', Times, serif;\">" + template  + "</p><button onclick='copyText(" + indexR.toString() +");'>copy</button></div>";
	for (i in search_results){
		indexR = search_results[i];
		template = words[indexR] + " - " + definition[indexR];
		char_out += "<div id='output1'><p style=\"font-family: 'Times New Roman', Times, serif;\">" + template  + "</p><button onclick='copyText(" + indexR.toString() +");'>copy</button></div>";
	}
	term_search = "";
	// Ouputs the output
	$("#Output").html(char_out);
};

