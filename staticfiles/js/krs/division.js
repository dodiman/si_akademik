function hapus_element(id_element) {
    // mengecek apakah element sudah ada
    let element = document.getElementById(id_element);
    if (element) {
        element.remove();
    }
}

function loading(id_element="loading") {
    let class_element = id_element;

    hapus_element(id_element);

    const div_elm = document.createElement("div");
    div_elm.setAttribute("id", id_element);
    div_elm.classList.add(class_element);

    div_elm.innerHTML = `Loading...`;
    
    document.body.appendChild(div_elm);
}

function pesan_error(id_element="pesan_error") {
    let class_element = id_element;

    hapus_element(id_element);

    const div_elm = document.createElement("div");
    div_elm.setAttribute("id", id_element);
    div_elm.classList.add(class_element);

    div_elm.innerHTML = `NIM tidak ditemukan`;
    
    document.body.appendChild(div_elm);
}

function info_mahasiswa(data_mahasiswa) {
    let id_element = "info_mahasiswa";
    let class_element = "info_mahasiswa";

    hapus_element(id_element);

    const div_elm = document.createElement("div");
    div_elm.setAttribute("id", id_element);
    div_elm.classList.add(class_element);

    div_elm.innerHTML = `<strong>Nama: ${data_mahasiswa.nama}</strong> <br> <strong>NIM: ${data_mahasiswa.nim}</strong>`;
    
    document.body.appendChild(div_elm);
}



function list_matakuliah(arr=[], id="list_matakuliah") {
    hapus_element(id);

    const div_elm = document.createElement("div");
    div_elm.setAttribute("id", id);
    document.body.appendChild(div_elm);

    const form_pilihan_matakuliah = form_checkbox_matakuliah(arr);
    div_elm.appendChild(form_pilihan_matakuliah);
}
