<script>
  import { Router, Route } from "svelte-routing";

  import Signup from "./components/signup.svelte";
  import Login from "./components/login.svelte";
  import Home from "./components/home.svelte";
  import ServerMessages from "./components/entries/serverMessages.svelte";
  import PageNotFound from "./components/pageNotFound.svelte";
  import PageTransition from "./components/pageTransition.svelte";
</script>

<ServerMessages />
<!-- <SocketData /> -->
<Router>
  <PageTransition>
    <Route path="/signup" component={Signup} />
    <Route path="/login" component={Login} />
  </PageTransition>
  <Route path="/home" component={Home} />
  <Route path="/">
    <h1>Hallo</h1>
  </Route>
  <Route path="" component={PageNotFound} />
</Router>
