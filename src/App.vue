<template>
    <div id="app">

        <UploadPage v-if="loginEd" v-bind:userInfo="userInfo"></UploadPage>
        <LoginPage v-else v-on:login="login"></LoginPage>
    </div>
</template>

<script>

    import UploadPage from "@/components/UploadPage";
    import LoginPage from "@/components/LoginPage";
    export default {
        name: 'App',
        components: {LoginPage, UploadPage},
        beforeMount() {

        },
        data() {
            return {
                loginEd:false,
                userInfo:{},
            }
        },
        methods: {
            login(e){
                this.userInfo=e
                this.loginEd=true
            }
        }
    }
</script>

<style>

    #app {
        height: calc(100vh);
        display: flex;
        flex-direction: column;
        background-color: rgb(242, 248, 242);
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;

    }
</style>
