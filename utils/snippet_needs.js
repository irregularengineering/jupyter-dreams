// clear cell at index 0
Jupyter.notebook.delete_cell(0)
Jupyter.notebook.insert_cell_at_index('code', 0)


// target the first cell to add "code"
var code = "here is an example of text/code we can add"
var new_cell = Jupyter.notebook.insert_cell_above('code', index=0);
            new_cell.set_text(code);
            new_cell.focus_cell();


// execute selected cells
Jupyter.notebook.execute_cells([0,1])


// hide a specific cell by index

var toggle_selected_input = function () {
    // Find the selected cell
    var cell = Jupyter.notebook.get_cell(0);
    // Toggle visibility of the input div
    cell.element.find("div.input").toggle('slow');
    cell.metadata.hide_input = ! cell.metadata.hide_input;
};

toggle_selected_input()

