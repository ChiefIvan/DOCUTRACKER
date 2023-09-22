<script>
  import { Router, Route } from "svelte-routing";
  import { serverResponse } from "./stores";

  import Signup from "./components/signup.svelte";
  import Login from "./components/login.svelte";
  import Home from "./components/home.svelte";
  import ServerMessages from "./components/entries/serverMessages.svelte";
  import PageNotFound from "./components/pageNotFound.svelte";
  import PageTransition from "./components/winEvents/pageTransFly.svelte";
  import ForgotPassword from "./components/forgotPassword.svelte";
  import { beforeUpdate } from "svelte";

  beforeUpdate(() => {
    if (String(Object.keys($serverResponse)).length !== 0) {
      setTimeout(() => {
        $serverResponse = {};
      }, 8000);
    }
  });
</script>

<ServerMessages />
<!-- <SocketData /> -->
<Router>
  <PageTransition>
    <Route path="/signup" component={Signup} />
    <Route path="/login" component={Login} />
  </PageTransition>
  <Route path="/home" component={Home} />
  <Route path="/Authentication/ResetPassword" component={ForgotPassword} />
  <Route path="/">
    <h1>Hallo</h1>
  </Route>
  <Route path="" component={PageNotFound} />
</Router>
