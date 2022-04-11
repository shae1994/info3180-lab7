<template>

<form @submit.prevent="uploadPhoto" enctype="multipart/form-data"  id="uploadForm">

<div class = "formers">
<h1>UploadForm</h1>
<br> 
<div class="form-label">Upload Photo</div>
    <input name="photo" type="file" class="form-control" />
    <div class="form-label">Description</div>
        <textarea name="description" type="text" class="form-control" /><br>
    <button type="submit" class="btn btn-primary">Submit</button> 
    </div>
</form>
</template>

<script>
    export default {
        data() {
            return {
            csrf_token: "",
            response: null,
            };
        },
    methods: {
    uploadPhoto() {
        const uploadForm = document.getElementById("uploadForm");
        let form_data = new FormData(uploadForm);
        fetch("/api/upload", {
            method:"POST",
            body: form_data,
            headers: {"X-CSRFToken": this.csrf_token}
        })
        .then((response) => response.json())
    }, 
    created() {
    this.getCsrfToken();
    },
        getCsrfToken() {
            let self = this;
            fetch('/api/csrf-token')
                .then((response) => response.json())
                .then((data) => {
            console.log(data);
            self.csrf_token = data.csrf_token;
            })
        }
    }
};
</script>



<style>
.formers{
    padding: 0% 5%;
}
</style>