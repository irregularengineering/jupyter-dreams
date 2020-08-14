""" Stash for custom JS """

CUSTOM_SNIPPIT_MENU_CODE = """
require(["nbextensions/snippets_menu/main"], function (snippets_menu) {
    console.log('Loading `snippets_menu` customizations from `custom.js`');
    var horizontal_line = '---';
    var docs = {
        'name' : 'Example - Utils',
        'sub-menu' : [
            {
                "name" : "API Docs",
                "external-link" : "docs/build/html/py-modindex.html"
            },
        ],
    };
    var styles = {
        'name' : 'Styling',
        'sub-menu' : [
            {
                "name" : "Reset CSS",
                "snippet" : ["",
                            "# reset your kernal afterwards",
                            "!rm /usr/local/lib/python3.6/site-packages/notebook/static/custom/custom.css",
                            ""]
            },
            {
                "name" : "Reset JS",
                "snippet" : ["",
                            "# reset your kernal afterwards",
                            "!rm /usr/local/lib/python3.6/site-packages/notebook/static/custom/custom.js",
                            ""]
            },
        ],
    };
    var itemone = {
        'name' : 'item one',
        'sub-menu' : [
            {
                "name" : "Something will go here ",
                "snippet" : ["",
                            "#1st step: Put something here",
                            ""]
            },
        ],
    };
    var itemtwo = {
        'name' : 'item two',
        'sub-menu' : [
            {
                "name" : "Something will go here ",
                "snippet" : ["",
                            "#1st step: Put something here",
                            ""]
            },
        ],
    };

    snippets_menu.options['menus'].push(itemone);

    snippets_menu.options['menus'].push(itemtwo);

    console.log('Loaded `snippets_menu` customizations from `custom.js`');
});

function execute_selected_cell() {
    console.log('Loading `execute_selected_cell` customizations from `custom.js`');
    require(['base/js/namespace'], function (jupyter) {
        jupyter.notebook.execute_selected_cells();
    });
}

function interrupt_kernel() {
    console.log('Loading `interrupt_kernel` customizations from `custom.js`');
    require(['base/js/namespace'], function (jupyter) {
        jupyter.notebook.kernel.interrupt();
    });
}

define(['base/js/namespace', 'base/js/events', 'notebook/js/codecell'], function (jupyter, events, cell) {

    cell.CodeCell.input_prompt_function = function (value, lines_number) {
        if (value === undefined || value === null) {
            return '<button class="btn btn-default btn-sm" onclick="execute_selected_cell()"><i class="fa fa-play"></i></button>&nbsp;';
        } else if(value === '*') {
            return '<button class="btn btn-danger btn-sm" onclick="interrupt_kernel()">stop <i class="fa fa-stop"></i></button>&nbsp;';
        } else {
            return '<button class="btn btn-default btn-sm" onclick="execute_selected_cell()">' + value + '&nbsp;<i class="fa fa-play"></i></button>&nbsp;';
        }
    };

    console.log('removing extraneous menus on top');
    $('#help_menu').parent().hide();
    console.log('done with killing extraneous menus on top');

});

"""
