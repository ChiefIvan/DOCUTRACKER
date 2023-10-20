<script>
  import { Router, Route, Link } from "svelte-routing";
  import { serverResponse, location } from "./stores";
  import { beforeUpdate } from "svelte";

  import Signup from "./components/routes/signup.svelte";
  import Login from "./components/routes/login.svelte";
  import Home from "./components/routes/home.svelte";
  import ServerMessages from "./components/entries/serverMessages.svelte";
  import PageNotFound from "./components/routes/pageNotFound.svelte";
  import PageTransition from "./components/winEvents/pageTransition.svelte";
  import ForgotPassword from "./components/routes/forgotPassword.svelte";
  import SideBar from "./components/main/sideBar.svelte";
  import Header from "./components/main/header.svelte";
  import Overview from "./components/routes/overview.svelte";

  beforeUpdate(() => {
    if (String(Object.keys($serverResponse)).length !== 0) {
      setTimeout(() => {
        $serverResponse = {};
      }, 8000);
    }
  });
</script>

<ServerMessages />
<Router basepath="/">
  <div>
    {#if $location === "/home"}
      <SideBar />
    {/if}

    <div class="head-wrapper">
      {#if $location === "/home"}
        <Header />
      {/if}

      <PageTransition>
        <Route path="auth/u/signup" component={Signup} />
        <Route path="auth/u/login" component={Login} />
        <Route path="auth/u/reset" component={ForgotPassword} />
        <Route path="home" component={Home} />
        <Route path="/" component={Overview} />
        <Route path="" component={PageNotFound} />
      </PageTransition>
    </div>
  </div>
</Router>

<style>
  div {
    display: flex;

    & div.head-wrapper {
      display: flex;
      flex-direction: column;
      width: 100%;
    }
  }
</style>
