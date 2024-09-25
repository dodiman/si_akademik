const csrf_token = document.querySelector('meta[name="csrf-token"]').getAttribute('content');


function form_data_mahasiswa() {    

    const form_elm = document.createElement("form");
    form_elm.setAttribute("id", "form_data_mahasiswa");
    form_elm.classList.add("form_data_mahasiswa");

    const label_elm = document.createElement("label");
    label_elm.textContent = "NIM";

    const input_elm = document.createElement("input");
    input_elm.setAttribute("placeholder", "Masukkan NIM...");
    input_elm.setAttribute("name", "nim");

    const button_elm = document.createElement("button");
    button_elm.setAttribute("type", "submit");
    button_elm.textContent = "Oke";

    form_elm.appendChild(label_elm);
    form_elm.appendChild(input_elm);
    form_elm.appendChild(button_elm);
    
    document.body.appendChild(form_elm);
    
}

async function form_penawaran_matakuliah(id="penawaran_matakuliah") {
    const form_elm = document.createElement("form");
    form_elm.setAttribute("id", id);
    form_elm.classList.add(id);

    document.body.appendChild(form_elm);

    const label_elm = document.createElement("label");
    label_elm.setAttribute("for", "pilih_semester");
    label_elm.textContent = "Pilih Matakuliah";

    const select_elm = document.createElement("select");
    select_elm.setAttribute("name", "semester");
    select_elm.setAttribute("id", "pilih_semester");

    const option_elm = document.createElement("option");
    option_elm.setAttribute("value", "");
    option_elm.textContent = "Silakan Pilih";

    // append child
    form_elm.appendChild(label_elm);
    select_elm.appendChild(option_elm);

    // perulangan
    const mydata = [
        {"id": 1, "semester": "I"},
        {"id": 2, "semester": "II"},
        {"id": 3, "semester": "III"},
        {"id": 4, "semester": "IV"},
        {"id": 5, "semester": "V"},
        {"id": 6, "semester": "VI"},
        {"id": 7, "semester": "VII"},
        {"id": 8, "semester": "VIII"},
    ]
    if (mydata !== null) {
        for (let i = 0; i < mydata.length; i++) {

            const option1 = document.createElement("option");
            option1.setAttribute("value", mydata[i]["semester"]);
            option1.textContent = mydata[i]["semester"];
            
            select_elm.appendChild(option1);
            
        }
    }
    
    form_elm.appendChild(select_elm);

    
}


function form_checkbox_matakuliah(arr=[], id="checkbox_matakuliah") {
    const my_form_elm = document.createElement("myform");
    my_form_elm.setAttribute("id", id);

    if (arr.length > 0) {
        for (let i = 0; i < arr.length; i++) {
            
            let id_checkbox = `matakuliahnya_${i}`

            const input_elm = document.createElement("input");
            input_elm.setAttribute("type", "checkbox");
            input_elm.setAttribute("id", id_checkbox);
            input_elm.setAttribute("name", "matakuliahnya");
            input_elm.setAttribute("value", arr[i]["nama"]);
            
            const label_elm = document.createElement("label");
            label_elm.setAttribute("for", id_checkbox);
            label_elm.textContent = arr[i]["nama"]


            my_form_elm.appendChild(input_elm);
            my_form_elm.appendChild(label_elm);
        }
    }

    return my_form_elm;
}


