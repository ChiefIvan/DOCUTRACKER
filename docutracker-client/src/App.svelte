<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import { location, showMessage, type ResponseData } from "./store";

  import Overview from "./components/routes/Overview.svelte";
  import Login from "./components/routes/Login.svelte";
  import Signup from "./components/routes/Signup.svelte";
  import Reset from "./components/routes/Reset.svelte";
  import Dashboard from "./components/routes/Dashboard.svelte";
  import NavigationLocation from "./components/lib/NavigationLocation.svelte";
  import _Error from "./components/routes/Error.svelte";
  import DisplayMessage from "./components/lib/ShowMessage.svelte";
  import Footer from "./components/lib/Footer.svelte";
  import Header from "./components/lib/Header.svelte";
  import DomEvents from "./components/lib/DOMEvents.svelte";
  import SideBar from "./components/lib/SideBar.svelte";

  let show: boolean = false;
  let user: ResponseData = {};
  let id: number | undefined;

  $: if (Object.keys($showMessage).length !== 0) {
    clearTimeout(id);
    show = true;

    id = setTimeout(() => {
      show = false;
    }, 8000);
  }

  const handleUser = (event: { detail: ResponseData }) => {
    user = event.detail;
  };
</script>

{#if show}
  <DisplayMessage responseMessage={$showMessage} />
{/if}

<Router basepath="/">
  <div class="side-main-wrapper">
    {#if $location === "/dashboard"}
      <SideBar />
    {/if}

    <div class="main-wrapper">
      <DomEvents />
      <Header {user} />

      <Route path="" component={_Error} />
      <Route path="/" component={Overview} />
      <Route path="/dashboard">
        <Dashboard on:user={handleUser} />
      </Route>
      <Route path="/auth/login/" component={Login} />
      <Route path="/auth/signup" component={Signup} />
      <Route path="/auth/reset" component={Reset} />

      <NavigationLocation />
    </div>
  </div>
</Router>

{#if $location === "/auth/login" || $location === "/auth/signup" || $location === "/auth/reset"}
  <Footer />
{/if}

<style>
  :global(body) {
    transition: all ease-in-out 100ms;
  }

  div.side-main-wrapper {
    display: flex;

    & div.main-wrapper {
      width: 100%;
    }
  }
</style>
