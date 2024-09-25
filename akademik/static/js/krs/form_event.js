async function form_data_mahasiswa_event() {
    const my_form = document.getElementById("form_data_mahasiswa");
    my_form.addEventListener("submit", (e) => {
        e.preventDefault();

        let form_data = new FormData(my_form);
        let params = Object.fromEntries(form_data.entries());
        
        cari_mahasiswa("cari_mahasiswa", params);

        my_form.reset();
    });
}

async function form_penawaran_matakuliah_event() {
    const my_form = document.getElementById("penawaran_matakuliah");

    my_form.addEventListener("change", async (e) => {
        const form_data = new FormData(my_form);
        const data_form = Object.fromEntries(form_data.entries());
        console.log(data_form);

        const matakuliah = await cari_semester("cari_semester", data_form);
        if (matakuliah !== null) {
            list_matakuliah(matakuliah);
        }

    });
}