<template>
    <div class="container">
        <img style="width: 100vw;height: 50vw;" src="../assets/loginHeader.png"/>
        <div class="inputCard">
            <div class="inputBox">
                <input placeholder="         |      用户名" v-model="userId">
            </div>
            <div class="inputBox">
                <input placeholder="         |      密码" v-model="userName">
            </div>
            <div @click="login" class="buttonBox">登录</div>
        </div>
        <img src="../assets/loginBottom.png"/>
    </div>
</template>

<style scoped>
    .buttonBox {
        margin-top: 15px;
        border: 1px solid #dee1de;
        border-radius: 10px;
        height: 45px;
        line-height: 40px;
        width: 82vw;
    }

    input {
        border: 1px solid #dee1de;
        border-radius: 4px;

        height: 30px;
        width: 80vw;
    }

    .inputBox {
        margin-top: 11px;
    }

    .inputCard {
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 30px 20px 0px 20px;
        margin-bottom: 15px;
    }

    .container {
        display: flex;
        flex-direction: column;
    }
</style>

<script>
    export default {
        name: "LoginPage",
        data() {
            return {
                userName: "",
                userId: "",
            }
        },
        methods:{
            login(){
                let args={userName:this.userName,userId:this.userId}
                this.$emit("login",args);
            }
        }
    }
</script>


