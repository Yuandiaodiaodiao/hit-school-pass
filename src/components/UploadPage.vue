<template>
    <div id="app1">
        <div class="header">
            <div id="info-title">
                <div id="title1">{{userInfo.userName}}</div>
                <div id="title2">{{userInfo.userId}}</div>
            </div>
            <img id="logoutImg" @click="logout" src="../assets/logout.png"/>
        </div>
        <div class="contentBox" id="box1">
            <div id="infotitle">位置信息</div>
            <div id="infodetail">
                <div>楼宇 : {{pos}}</div>
                <div>日期 : {{nowTime}}</div>
            </div>
            <div class="line"></div>

            <div v-show="buttonType==='进入'" @click="toSuccess" class="greenButton">进入</div>
            <div v-show="buttonType==='成功'" @click="toEnter" v-longpress="lock" class="blueButton">上报位置成功</div>
        </div>
        <div class="contentBox" id="box2">
            <div id="todayUpload">今日上报</div>
            <div class="line2"></div>
            <div class="uploadBox" v-for="(item,i) in uploadData" :key="i">
                <div class="uploadTime">{{item.time}}</div>
                <div class="uploadPos">{{item.pos}}</div>
            </div>
        </div>
    </div>
</template>

<script>
    import "../utils/util"

    export default {
        name: 'UploadPage',
        components: {},
        beforeMount() {
            this.nowTime = new Date().format("yyyy-MM-dd hh:mm")
        },
        props: {
            userInfo: {
                type: Object,
                required: true
            }
        },
        data() {
            return {
                nowTime: "",
                buttonType: "进入",
                pos: "学校南门出(限制2次)",
                inOrOut: "进入",
                uploadData: [
                    // {
                    //     time:"上报时间:2020-09-12 18:21",
                    //     pos:"学校南门出(限制两次) | 进入"
                    // }
                ],
                islock:false,
            }
        },
        methods: {
            toSuccess() {

                let formatStr = "yyyy-MM-dd hh:mm";
                let time = new Date().format(formatStr)
                this.nowTime = time
                let pos=this.pos
                if(this.uploadData.length===0){
                    pos=pos.replace("出","进")
                }else{
                    this.uploadData.forEach(item=>{
                        const time=item.time.split("：")[1]
                        const date=new Date(time)
                        const newDate=date.getTime()-1000*3600
                        const newTime=new Date(newDate).format(formatStr)
                        item.time="上报时间 ：" + newTime
                    })
                }
                this.uploadData.unshift(
                    {
                        time: "上报时间 ：" + time,
                        pos: pos + " | " + this.inOrOut
                    }
                )
                this.buttonType = "成功"
            },
            toEnter() {
                if(this.islock){
                    return
                }
                this.buttonType = "进入"

            },
            logout(){
                this.buttonType = "进入"
                this.$emit('logout')
            },
            lock(){
                console.log("lock",this.islock)
                this.islock=!this.islock
            }
        }
    }
</script>

<style>
    #info-title #title1 {
        font-size: 19px;
        font-weight: 500;
    }

    #info-title #title2 {
        font-size: 16px;
        font-weight: lighter;
        letter-spacing: -0.5px;

    }
    #info-title {
        text-align: left;
        margin-left: 17px;
        margin-top: 9px;
    }

    .header {
        display: flex;
        align-items: flex-end;
        justify-content: space-between;
        color: #f7ffff;
        background-color: #087dbf;
        box-shadow: 0 0 1px 1px #cecece;
    }
    #logoutImg {
        height: 32px;
        width: 90px;
    }

    #todayUpload {
        margin-left: 1.5px;
        padding: 15px;
        font-size: 13px;
        color: #000000;
        font-weight: 500;
    }

    .uploadBox {
        margin-left: 16px;
        line-height: 20px;
        margin-bottom: 50px;
    }

    .uploadBox .uploadTime {
        font-size: 15px;
        font-weight: 500;
        color: #000000;
        margin-bottom: 4px;
    }

    .uploadBox .uploadPos {
        font-size: 12px;
        color: rgb(128, 132, 128);
        letter-spacing: 0.5px;

    }

    .contentBox #infotitle {
        font-weight: bolder;
        font-size: 15px;
        margin-bottom: 8px;
        margin-top: 15px;
    }

    .contentBox #infodetail {
        line-height: 19px;
        font-size: 12.5px;

        color: rgb(174, 179, 173);
    }

    #box1 {
        padding: 0px 17px;
    }

    #box2 {
        height: 400px;
        overflow: hidden;
    }

    .contentBox {
        text-align: left;
        margin-top: 10px;
        box-shadow: 0 0 1px 1px #fcfcfc;
        background-color: rgb(255, 255, 255);
    }

    .blueButton {
        font-size: 15px;
        margin: 20px auto 20px auto;
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
        margin-top:2px;
        background-color: rgba(206, 206, 206, 0.17);
        height: 1px;
    }
    .line2 {
        margin-top:2px;
        background-color: rgba(206, 206, 206, 0.17);
        height: 1px;
        margin-bottom: 30px;

    }



    #app1 {
        height: calc(100vh);
        display: flex;
        flex-direction: column;
        background-color: rgb(245, 245, 245);
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;

    }




</style>
