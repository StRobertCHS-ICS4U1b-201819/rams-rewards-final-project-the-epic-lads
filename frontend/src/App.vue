<template>
<div style="background-color:#E3E5E7;">

    <div style="margin:0 auto;max-width:600px;background:#FF8A2BE2;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:rgba(241,241,241,0.8);" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:20px 0px;">
              <div aria-labelledby="mj-column-per-100" class="mj-column-per-100" style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                <table cellpadding="0" cellspacing="0" style="vertical-align:top;" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td style="word-break:break-word;font-size:0px;padding:10px 25px;" align="center">
                        <table cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px;" align="center" border="0">
                          <tbody>
                            <tr>
                              <td style="width:80px;"><a href="about:blank" target="_blank"><img alt="auth0" title="" height="auto" src="https://pbs.twimg.com/profile_images/1541158612/YCDSB_Logo_400x400.png" style="border:none;border-radius:;display:block;outline:none;text-decoration:none;width:100%;height:auto;" width="80"></a></td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="margin:0 auto;max-width:600px;background:#222228;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#222228;" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:20px 0px;">

              <div aria-labelledby="mj-column-per-80" class="mj-column-per-80" style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                <table cellpadding="0" cellspacing="0" style="vertical-align:top;" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td style="word-break:break-word;font-size:0px;padding:10px 25px;padding-top:30px;" align="center">
                        <table cellpadding="0" cellspacing="0" style="border-collapse:collapse;border-spacing:0px;" align="center" border="0">
                          <tbody>
                            <tr>
                              <td style="width:80px;"><qrcode-stream height="120" style="border:none;border-radius:;display:block;outline:none;text-decoration:none;width:100%;height:auto;" width="120" @decode="onDecode" @init="onInit" /></td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                    <tr>
                      <td style="word-break:break-word;font-size:0px;padding:0px 20px 0px 20px;" align="center">
                        <div style="cursor:auto;color:white;font-family:'Avenir Next', Avenir, sans-serif;font-size:32px;line-height:60ps;text-align:center">
                          Scan the QR code<br>
                          <p class="error">{{ error }}</p>
                          <p class="decode-result"><b>{{ result }}</b></p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin:0 auto;max-width:600px;background:white;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:white;" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:0px 30px;">

              <p style="font-size:1px;margin:0 auto;border-top:1px solid #E3E5E7;width:100%;"></p>

            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin:0 auto;max-width:600px;background:white;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:white;" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:20px 0px;">
              <div aria-labelledby="mj-column-per-100" class="mj-column-per-100" style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                <table cellpadding="0" cellspacing="0" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td style="word-break:break-word;font-size:0px;padding:10px 25px;" align="center">
                        <table cellpadding="0" cellspacing="0" align="center" border="0">
                          <tbody>
                            <tr>
                              <td v-if="!authenticated" @click="login()" style="border-radius:3px;color:white;cursor:auto;" align="center" valign="middle" bgcolor="#EB5424">
                                <a style="display:inline-block;text-decoration:none;background:#EB5424;border-radius:3px;color:white;font-family:'Avenir Next', Avenir, sans-serif;font-size:14px;font-weight:500;line-height:35px;padding:10px 25px;margin:0px;"
                                  >
                                                                    LOGIN TO YOUR ACCOUNT
                                                                </a>
                                                                </td>
                                <td v-if="authenticated" @click="privateMessage()" style="border-radius:3px;color:white;cursor:auto;" align="center" valign="middle" bgcolor="#EB5424">
                                <a style="display:inline-block;text-decoration:none;background:#EB5424;border-radius:3px;color:white;font-family:'Avenir Next', Avenir, sans-serif;font-size:14px;font-weight:500;line-height:35px;padding:10px 25px;margin:0px;">Call Private </a> </td>
                            <div class="divider"/>
                            <td  v-if="authenticated" @click="logout()" style="border-radius:3px;color:white;cursor:auto;" align="center" valign="middle" bgcolor="#EB5424">
                                <a style="display:inline-block;text-decoration:none;background:#EB5424;border-radius:3px;color:white;font-family:'Avenir Next', Avenir, sans-serif;font-size:14px;font-weight:500;line-height:35px;padding:10px 25px;margin:0px;">Log Out </a> </td>
                            </tr>
                          </tbody>
                        </table>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="margin:0 auto;max-width:600px;background:white;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:white;" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:20px 0px;">

              <div aria-labelledby="mj-column-per-100" class="mj-column-per-100" style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                <table cellpadding="0" cellspacing="0" style="vertical-align:top;" width="100%" border="0">
                  <tbody>
                    <tr>
                    </tr>
                  </tbody>
                </table>
              </div>

            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div style="margin:0 auto;max-width:600px;background:#F5F7F9;">
      <table cellpadding="0" cellspacing="0" style="font-size:0px;width:100%;background:#F5F7F9;" align="center" border="0">
        <tbody>
          <tr>
            <td style="text-align:center;vertical-align:top;font-size:0px;padding:20px 0px;">

              <div aria-labelledby="mj-column-per-100" class="mj-column-per-100" style="vertical-align:top;display:inline-block;font-size:13px;text-align:left;width:100%;">
                <table cellpadding="0" cellspacing="0" style="vertical-align:top;" width="100%" border="0">
                  <tbody>
                    <tr>
                      <td style="word-break:break-word;font-size:0px;padding:0px 20px;" align="center">
                        <div style="cursor:auto;color:#222228;font-family:'Avenir Next', Avenir, sans-serif;font-size:13px;line-height:20px;">
                          <p class="error">{{ error }}</p>
                          <p class="decode-result">Last result: <b>{{ result }}</b></p>
                        </div>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

            </td>
          </tr>
        </tbody>
      </table>
    </div>

    <div></div>

  </div>
  <!--div>
    <div>
      <p class="error">{{ error }}</p>
      <p class="decode-result">Last result: <b>{{ result }}</b></p>
      <qrcode-stream @decode="onDecode" @init="onInit" />
    </div>
    <md-button
      class="md-raised md-primary"
      v-if="!authenticated"
      @click="login()">
      Log In
    </md-button>

    <md-button
      class="md-raised md-primary"
      v-if="authenticated"
      @click="privateMessage()">
      Call Private
    </md-button>

    <md-button
      class="md-raised md-primary"
      v-if="authenticated"
      @click="logout()">
      Log Out
    </md-button>
    {{message}}
    <br>
  </div-->
</template>
<script>
import AuthService from './auth/AuthService'
import axios from 'axios'
const API_URL = 'http://localhost:8000'
const auth = new AuthService()
export default {
  name: 'app',
  data () {
    this.handleAuthentication()
    this.authenticated = false

    auth.authNotifier.on('authChange', authState => {
      this.authenticated = authState.authenticated
    })

    return {
      authenticated: false,
      message: '',
      result: '',
      error: ''
    }
  },
  methods: {
    onDecode (result) {
      this.result = result
    },
    async onInit (promise) {
      try {
        await promise
      } catch (error) {
        if (error.name === 'NotAllowedError') {
          this.error = 'ERROR: you need to grant camera access permisson'
        } else if (error.name === 'NotFoundError') {
          this.error = 'ERROR: no camera on this device'
        } else if (error.name === 'NotSupportedError') {
          this.error = 'ERROR: secure context required (HTTPS, localhost)'
        } else if (error.name === 'NotReadableError') {
          this.error = 'ERROR: is the camera already in use?'
        } else if (error.name === 'OverconstrainedError') {
          this.error = 'ERROR: installed cameras are not suitable'
        } else if (error.name === 'StreamApiNotSupportedError') {
          this.error = 'ERROR: Stream API is not supported in this browser'
        }
      }
    },
    // this method calls the AuthService login() method
    login () {
      auth.login()
    },
    handleAuthentication () {
      auth.handleAuthentication()
    },
    logout () {
      auth.logout()
    },
    privateMessage () {
      const url = `${API_URL}/api/private/`
      return axios.get(url, {headers: {Authorization: `Bearer ${AuthService.getAuthToken()}`}}).then((response) => {
        console.log(response.data)
        this.message = response.data || ''
      })
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.error {
  font-weight: bold;
  color: red;
}
.qrcode-stream{
  position: flex;
  width:100%;
}
.divider{
    width:15px;
    height:auto;
    display:inline-block;
}
</style>
