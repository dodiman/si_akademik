const base_url = window.location.origin;
const app_url = "akademik/";

function menyusun_ulang_url(url) {
    const my_url = `${base_url}/${app_url}${url}`;
    return my_url;
}

async function cari_mahasiswa(url="cari_mahasiswa", params) {
    // const my_url = `${base_url}/${app_url}${url}`;
    const my_url = menyusun_ulang_url(url)
    
    try {
        hapus_element("pesan_error");
        loading();
        const response = await axios.get(my_url, {
            params: params,
            // headers: headers,
        });
        const data = response.data;
        
        hapus_element("loading");
        info_mahasiswa(data);

    } catch (error) {
        hapus_element("loading");
        hapus_element("info_mahasiswa");
        pesan_error();
        // console.log("terjadi kesalahan");
    }
    

}


async function matakuliah_service(url) {
    const my_url = menyusun_ulang_url(url);
    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.log("terjadi kesalahan matakuliah");
        return null;
    }
}

async function semester_service(url) {
    const my_url = menyusun_ulang_url(url);

    try {
        const response = await axios.get(url);
        const data = response.data;
        return data;
    } catch (error) {
        console.log("terjadi kesalahan dalam pengambilan data");
        return null;
    }
}

async function cari_semester(url, params) {
    const my_url = menyusun_ulang_url(url);

    try {
        const response = await axios.get(url, {
            params: params
        });
        const data = response.data;
        return data;
    } catch (error) {
        console.log("terjadi kesalahan dalam pengambilan data");
        return null;
    }
}