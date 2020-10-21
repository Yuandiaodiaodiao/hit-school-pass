<template>
    <div id="app">

        <UploadPage v-show="loginEd" v-bind:userInfo="userInfo" v-on:logout="logout"></UploadPage>
        <LoginPage v-show="!loginEd" v-on:login="login"></LoginPage>
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
            },
            logout(){
                this.loginEd=false
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
