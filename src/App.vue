<template>
    <div id="app">
        <div class="header">
            <div id="info-title">
                <div id="title1">王子溪</div>
                <div id="title2">2170200925</div>
            </div>
            <img id="logoutImg" src="./assets/logout.png"/>
        </div>
        <div class="contentBox" id="box1">
            <div id="infotitle">位置信息</div>
            <div id="infodetail">
                <div>楼宇 : {{pos}}</div>
                <div>日期 : {{nowTime}}</div>
            </div>
            <div class="line"></div>

            <div v-if="buttonType==='进入'" @click="toSuccess" class="greenButton">进入</div>
            <div v-if="buttonType==='成功'" @click="toEnter" class="blueButton">上报位置成功</div>
        </div>
        <div class="contentBox" id="box2">
            <div id="todayUpload">今日上报</div>
            <div class="line"></div>
            <div class="uploadBox" v-for="(item,i) in uploadData" :key="i">
                <div class="uploadTime">{{item.time}}</div>
                <div class="uploadPos">{{item.pos}}</div>
            </div>
        </div>
    </div>
</template>

<script>
    import "./utils/util"

    export default {
        name: 'App',
        components: {},
        beforeMount() {
            this.nowTime = new Date().format("yyyy-MM-dd hh:mm")
            this.toSuccess()
        },
        data() {
            return {
                nowTime: "",
                buttonType: "成功",
                pos: "学校南门出(限制2次)",
                inOrOut: "进入",
                uploadData: [
                    // {
                    //     time:"上报时间:2020-09-12 18:21",
                    //     pos:"学校南门出(限制两次) | 进入"
                    // }
                ]
            }
        },
        methods: {
            toSuccess() {
                let formatStr = "yyyy-MM-dd hh:mm";
                let time = new Date().format(formatStr)
                this.nowTime=time
                this.uploadData.push(
                    {
                        time: "上报时间 : "  + time,
                        pos: this.pos + " | " + this.inOrOut
                    }
                )
                this.buttonType = "成功"
            },
            toEnter() {
                this.buttonType = "进入"
                this.uploadData.length=0
            }
        }
    }
</script>

<style>
    #info-title #title1{
        font-size: 18px;
    }
    #info-title #title2{
        font-size: 16px;
        letter-spacing:-1px;
    }
    #logoutImg{
        height: 30px;
        width: 90px;
    }
    #todayUpload {
        padding: 15px;
        font-size: 14px;
        color: #000000;
        font-weight: 500;
    }

    .uploadBox {
        margin-top: 30px;
        margin-left: 16px;
        line-height: 20px;
    }

    .uploadBox .uploadTime {
        font-size: 15px;
        font-weight: 500;
        color: #000000;
        margin-bottom: 5px;
    }

    .uploadBox .uploadPos {
        font-size: 13px;
        color: rgb(128, 132, 128);
    }

    .contentBox #infotitle {
        font-weight: bolder;
        font-size: 15px;
        margin-bottom: 8px;
        margin-top: 15px;
    }

    .contentBox #infodetail {
        line-height: 19px;
        font-size: 12px;
        color: rgb(174, 179, 173);
    }

    #box1 {
        padding: 0px 17px;
    }

    #box2 {
        height: min(50vh, 400px);
        overflow: hidden;
    }

    .contentBox {
        text-align: left;
        margin-top: 10px;
        box-shadow: 0 0 1px 1px #fcfcfc;
        background-color: rgb(253, 255, 253);
    }

    .blueButton {
        font-size: 15px;
        margin: 23px auto 20px auto;
        text-align: center;
        line-height: 40px;
        height: 40px;
        width: 72vw;
        border-radius: 50px;
        color: #f7ffff;
        background-color: rgb(0, 128, 201);
    }

    .greenButton {
        margin: 10px auto;
        text-align: center;
        line-height: 100px;
        height: 100px;
        width: 100px;
        border-radius: 50px;
        color: #f7ffff;
        background-color: rgb(5, 204, 100);
    }

    .line {
        background-color: #cecece;
        height: 1px;
    }

    #info-title {
        text-align: left;
        margin-left: 18px;
        margin-top: 10px;
    }

    .header {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        color: #f7ffff;
        background-color: #087dbf;
        box-shadow: 0 0 1px 1px #cecece;
    }

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
