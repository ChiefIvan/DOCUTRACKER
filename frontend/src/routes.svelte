<script>
  import { Router, Route, Link } from "svelte-routing";
  import { serverResponse, location } from "./stores";
  import { beforeUpdate } from "svelte";

  import Signup from "./components/signup.svelte";
  import Login from "./components/login.svelte";
  import Home from "./components/home.svelte";
  import ServerMessages from "./components/entries/serverMessages.svelte";
  import PageNotFound from "./components/pageNotFound.svelte";
  import PageTransition from "./components/winEvents/pageTransFly.svelte";
  import ForgotPassword from "./components/forgotPassword.svelte";

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
<Router basepath="/">
  <PageTransition>
    <Route path="auth/u/signup" component={Signup} />
    <Route path="auth/u/login" component={Login} />
  </PageTransition>
  <Route path="home" component={Home} />
  <Route path="auth/u/reset" component={ForgotPassword} />
  <Route path="/">
    <button>
      <Link to="auth/u/signup">Signup</Link>
    </button>
    <button>
      <Link to="auth/u/login">Login</Link>
    </button>
  </Route>
  <Route path="" component={PageNotFound} />
</Router>
