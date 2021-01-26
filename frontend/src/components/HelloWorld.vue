<template>
  <div class="hello">
    <el-row>
      <!-- 左侧空白 -->
      <el-col :span="3"><div class="grid-content"></div></el-col>

      <el-col :span="18">
        <el-container>
          <!-- 头部 -->
          <el-header>
            <h2>
              <b>儿童标准体重身高在线查询</b>
            </h2>
          </el-header>

          <!-- 主部 -->
          <el-container style="height: 600px; border: 1px solid #eee">
            <!-- 左侧 -->
            <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
              <el-menu style="line-height:30px;">
                <el-submenu index="1">
                  <template slot="title"><i class="el-icon-message"></i>介绍</template>
                  <p class="paragraph-style">
                    <font>
                      《中国7岁以下儿童生长发育参照标准》由卫生部组织相关专家研究制订，
                      于2009年6月2日正式公布，
                      该标准包含了男童的身高、体重、头围、平均值标准和
                      女童的身高、体重、头围、平均值标准。
                    </font>
                  </p>
                </el-submenu>
                <el-submenu index="2">
                  <template slot="title"><i class="el-icon-menu"></i>说明</template>
                  <p class="paragraph-style">
                    <font>
                      “中位数”，表示处于人群的平均水平；
                      如果在“-1SD~~+1SD”即：
                      中位数上下一个标准差范围之内，属于“正常范围”，
                      代表了68%的儿童；如果在“（-2sd~-1sd）或者（+1sd~+2sd）”
                      即：中位数上下两个标准差范围之内，则定义为“偏矮（高）”，
                      代表了27.4%的儿童；如果在
                      “（-3sd~-2sd）或者（+2sd~+3sd）”即：
                      中位数上下三个标准差之内，则定义为“矮（高）”，
                      代表了4.6%的儿童。极少儿童在三个标准差之外（比例小于0.5%）。
                    </font>
                  </p>
                </el-submenu>
                
              </el-menu>
            </el-aside>

            <!-- 查询框 -->
            <el-main>
              <div class="grid-content form-style">
                <h1>
                  <font><b>请选择儿童信息</b></font>
                </h1>
                <!-- 表单开始 -->
                <el-form :model="form" ref="form" :rules="rules" 
                  label-width="100px" style="margin-bottom: 50px;">
                  <!-- 性别选择 -->
                  <el-form-item label="性别" prop="gender">
                    <el-radio-group v-model="form.gender">
                      <el-radio-button label="男孩" name="boy"></el-radio-button>
                      <el-radio-button label="女孩" name="girl"></el-radio-button>
                    </el-radio-group>
                  </el-form-item>
                  <!-- 出生日期选择 -->
                  <el-form-item label="出生日期" prop="datevalue">
                    <el-date-picker
                      v-model="form.datevalue"
                      align="right"
                      type="date"
                      placeholder="选择日期"
                      :picker-options="pickerOptions">
                    </el-date-picker>
                  </el-form-item>

                  <el-form-item>
                    <el-button type="primary" @click="OnSubmit('form')" value="submit" icon="el-icon-search">查询</el-button>
                    <el-button @click="resetForm('form')">重置</el-button>
                    <el-button v-if="std.length" style="margin-left: 100px;" type="danger" 
                      icon="el-icon-delete" @click="std=[]">清除记录</el-button>
                  </el-form-item>
                </el-form>
                <!-- 表单结束 -->

                <div class="grid-content">
                  <div v-for="(item, index) in std" :key="item">
                    <!-- 卡片 -->
                    <el-card class="cardstyle" shadow="hover" v-loading="!index && loading">
                      <!-- 卡片头部 -->
                      <div slot="header" class="clearfix">
                        <label><b> 查询结果 </b></label>
                        <label for="" style="margin-left: 3em;"><b>性别</b>:{{item.gender}}
                          <svg v-if="item.boyicon" t="1610798153327" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="656" width="16" height="16"><path d="M744.727273 651.636364c0-205.661091-166.702545-372.363636-372.363637-372.363637S0 445.975273 0 651.636364s166.702545 372.363636 372.363636 372.363636 372.363636-166.702545 372.363637-372.363636zM93.090909 651.636364c0-154.228364 125.044364-279.272727 279.272727-279.272728s279.272727 125.044364 279.272728 279.272728-125.044364 279.272727-279.272728 279.272727S93.090909 805.864727 93.090909 651.636364z" fill="#1296db" p-id="657"></path><path d="M857.344 93.090909H698.181818a46.545455 46.545455 0 0 1 0-93.090909h279.272727a46.545455 46.545455 0 0 1 46.545455 46.545455v279.272727a46.545455 46.545455 0 0 1-93.090909 0V166.656L632.110545 465.454545 558.545455 391.889455 857.344 93.090909z" fill="#1296db" p-id="658"></path></svg>
                          <svg v-else t="1610798814548" class="icon" viewBox="0 0 1024 1024" version="1.1" xmlns="http://www.w3.org/2000/svg" p-id="1107" width="16" height="16"><path d="M554.666667 680.021333V768h128a42.666667 42.666667 0 0 1 0 85.333333h-128v128a42.666667 42.666667 0 0 1-85.333334 0v-128h-128a42.666667 42.666667 0 0 1 0-85.333333h128v-87.978667C300.949333 659.029333 170.666667 515.413333 170.666667 341.333333 170.666667 152.810667 323.477333 0 512 0s341.333333 152.810667 341.333333 341.333333c0 174.08-130.282667 317.696-298.666666 338.688zM256 341.333333c0 141.376 114.624 256 256 256s256-114.624 256-256S653.376 85.333333 512 85.333333 256 199.957333 256 341.333333z" fill="#d4237a" p-id="1108"></path></svg>
                        </label>
                        <label for="" style="margin-left: 3em"><b>月龄</b>:{{item.moonage}}</label>
                        <label for="" style="margin-left: 3em"><b>查询时间</b>:{{item.querytime}}</label>
                        <el-button style="float: right" icon="el-icon-delete" type="info" size="mini" circle
                          @click="removeItem(item)"></el-button>
                      </div>
                      <!-- 表格 -->
                      <el-table
                        :data="item.table"
                        style="width: 100%">
                        <el-table-column
                          prop="item"
                          label="项目"
                          width="120">
                        </el-table-column>
                        <el-table-column
                          prop="SDd3"
                          label="-3SD"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SDd2"
                          label="-2SD"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SDd1"
                          label="-1SD"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SD0"
                          label="中位数"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SD1"
                          label="1SD"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SD2"
                          label="2SD"
                          width="100">
                        </el-table-column>
                        <el-table-column
                          prop="SD3"
                          label="3SD"
                          width="100">
                        </el-table-column>
                      </el-table>
                    </el-card>
                  </div>
                </div>
              </div>
            </el-main>
          </el-container>

        </el-container>
      </el-col>

      <!-- 右侧空白 -->
      <el-col :span="3"><div class="grid-content"></div></el-col>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      form: {
        gender: '',
        datevalue: ''
      },
      std: [],
      loading: false,
      // 日期选择框
      pickerOptions: {
        disabledDate (time) {
          return ( time.getTime() > Date.now() ) || ( time.getTime() + 3600 * 1000 * 24 * 30 * 81 < Date.now() )
        },
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      },
      // 表单规则
      rules: {
        datevalue: [
          { type: 'date', required: true, trigger: 'change', message: '请选择出生日期'}
        ],
        gender: [
          { required: true, message: '请选择儿童性别', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    OnSubmit (form) {
      var submit = false
      this.$refs[form].validate((valid) => {
        if (valid) {
          submit = true;
        } else {
          return false;
        }
      })
      if ( submit == true ){
        this.axios({
          method: 'post',
          url: '/formdata',
          data: this.form
        })
          .then((response) => {
            // 加载条
            this.loading = true
            setTimeout(() => {
              this.loading = false
            }, 200)
            
            // 格式处理数据
            var result = response.data
            var item = {}
            item.querytime = result.querytime
            item.gender = result.gender
            item.moonage = result.moonage
            item.table = []
            item.table.push(result.height)
            item.table.push(result.weight)
            item.boyicon = result.gender==='男孩' ? 1 : 0
            this.std.unshift(item)
            
            // 消息提示
            this.$message({
              message: '查询成功',
              type: 'success'
            })
          })
          .catch((error) => {
            console.log(error)
            // 消息提示
            this.$message({
              message: '出错啦！检查一下后端吧',
              type: 'error'
            })
          })
      }
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    removeItem(itemName) {
      var index = this.std.indexOf(itemName)
      console.log(index)
      if ( index > -1 )
        return this.std.splice(index, 1)
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
  .el-row {
    margin-bottom: 20px;
  }
  .grid-content {
    min-height: 36px;
  }
  .form-style {
    padding-left: 40px;
    text-align: left;
    border-radius: 8px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding-top: 40px;
    height: 260px;
  }
  .el-col {
    border-radius: 4px;
  }
  h1, h2 {
    font-weight: normal;
  }

  .el-header {
    background-color: #B3C0D1;
    color: #333;
    /* height: 90px; */
    text-align: center;
    /* line-height: 60px; */
  }

  .el-aside {
    background-color: #D3DCE6;
    color: #333;
    text-align: center;
    line-height: 200px;
  }

  .el-main {
    /* background-color: #E9EEF3; */
    color: #333;
    text-align: center;
    min-height: 600px;
    /* line-height: 60px; */
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .el-container:nth-child(5) .el-aside,
  .el-container:nth-child(6) .el-aside {
    line-height: 60px;
  }

  .el-container:nth-child(7) .el-aside {
    line-height: 120px;
  }
  .paragraph-style {
    text-indent:2em;
    text-align: left;
    margin: 1em;
  }
  .box-card {
    width: 100%;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }
  .cardstyle {
    margin-left: -40px;
    margin-top: 20px;
  }
</style>
