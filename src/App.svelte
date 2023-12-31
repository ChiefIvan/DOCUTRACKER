<script lang="ts">
  import { Router, Route } from "svelte-routing";
  import {
    location,
    showMessage,
    notificationExpand,
    registrationExpand,
    handleFetch,
    address,
    dark,
    type ResponseData,
    type RequestAPI,
    type DocumentPath,
  } from "./store";
  import { fly } from "svelte/transition";
  import { afterUpdate } from "svelte";

  import Overview from "./components/routes/Overview.svelte";
  import Login from "./components/routes/Login.svelte";
  import Signup from "./components/routes/Signup.svelte";
  import Reset from "./components/routes/Reset.svelte";
  import Dashboard from "./components/routes/Dashboard.svelte";
  import Updates from "./components/routes/History.svelte";
  import NavigationLocation from "./components/lib/NavigationLocation.svelte";
  import _Error from "./components/routes/Error.svelte";
  import DisplayMessage from "./components/lib/ShowMessage.svelte";
  import Footer from "./components/lib/Footer.svelte";
  import Header from "./components/lib/Header.svelte";
  import DomEvents from "./components/lib/DOMEvents.svelte";
  import SideBar from "./components/lib/SideBar.svelte";
  import UserRegistration from "./components/lib/UserRegistration.svelte";
  import Notification from "./components/routes/Notification.svelte";
  import Analytics from "./components/routes/Analytics.svelte";
  import DocumentOverview from "./components/routes/DocumentOverview.svelte";
  import ShortcutWrapper from "./components/shared/ShortcutWrapper.svelte";
  import AdminLogin from "./components/routes/AdminLogin.svelte";
  import AdminInterface from "./components/routes/AdminInterface.svelte";

  let show: boolean = false;
  let user: ResponseData = {};

  $: fullVerified = user.full_ver_val;
  $: allDocumentPath = user.documents;

  let id: string | number | NodeJS.Timeout | undefined;

  const authToken = sessionStorage.getItem("remember") || "";
  const indexMethod = "GET";
  const streamAddress = `${address}/index`;

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

  const streamRequest: RequestAPI = {
    method: indexMethod,
    address: streamAddress,
  };

  let intervalId: string | number | NodeJS.Timeout | undefined;

  afterUpdate(() => {
    if (
      $location === "/dashboard" ||
      $location === "/history" ||
      $location === "/notifications" ||
      $location === "/analytics" ||
      $location === "/document/overview"
    ) {
      if (intervalId) {
        clearInterval(intervalId);
      }

      intervalId = setInterval(async () => {
        const response: ResponseData = await handleFetch(
          streamRequest,
          authToken
        );

        user = response;
      }, 5000);
    }
  });

  let scan = false;
  let registerD = false;
  let registerR = false;
  let updateR = false;
  let shortcutData: string = "";

  const handleShortcutData = (event: { detail: string }) => {
    shortcutData = event.detail;

    if (shortcutData === "Scan Document") {
      scan = !scan;
      registerD = false;
      registerR = false;
      updateR = false;
    }

    if (shortcutData === "Register Document") {
      registerD = !registerD;
      scan = false;
      registerR = false;
      updateR = false;
    }

    if (shortcutData === "Register Route") {
      scan = false;
      registerD = false;
      registerR = !registerR;
      updateR = false;
    }

    if (shortcutData === "Update Route") {
      scan = false;
      registerD = false;
      registerR = false;
      updateR = !updateR;
    }
  };

  const handleNavigation = () => {
    scan = false;
    registerD = false;
    registerR = false;
    updateR = false;
  };

  $: if ($registrationExpand) {
    scan = false;
    registerD = false;
    registerR = false;
    updateR = false;
  }

  $: if (scan || registerD || registerR || updateR) {
    document.body.classList.add("disable-scroll");
    window.scrollTo(0, 0);
  } else {
    document.body.classList.remove("disable-scroll");
  }

  type DocumentData = {
    documentName: string;
    documentDescription: string;
    codeData: string;
    documentRegDate: string;
  };

  let documentData: DocumentData = {
    documentName: "",
    documentDescription: "",
    codeData: "",
    documentRegDate: "",
  };

  const handleDocumentData = (event: { detail: DocumentData }) => {
    documentData = event.detail;
  };

  $: console.log(user);
</script>

{#if show}
  <DisplayMessage responseMessage={$showMessage} />
{/if}

<Router basepath="/DOCUTRACKER">
  <div class="side-main-wrapper">
    {#if $location === "/dashboard" || $location === "/history" || $location === "/notifications" || $location === "/analytics" || $location === "/document/overview"}
      <SideBar on:switch={handleShortcutData} on:navActive={handleNavigation} />
    {/if}

    <div class="main-wrapper">
      <DomEvents />
      <Header {user} />

      {#if $registrationExpand}
        <UserRegistration />
      {/if}

      <Route path="" component={_Error} />
      <Route path="/" component={Overview} />
      <Route path="/admin">
        <AdminInterface></AdminInterface>
      </Route>
      <Route path="/dashboard">
        <Dashboard on:user={handleUser} {authToken} routes={allDocumentPath} />
      </Route>
      <Route path="/history">
        <Updates on:user={handleUser} {authToken}></Updates>
      </Route>
      <Route path="/notifications">
        <Notification on:user={handleUser} {authToken}></Notification>
      </Route>
      <Route path="/analytics">
        <Analytics on:user={handleUser} {authToken}></Analytics>
      </Route>
      <Route path="/document/overview">
        <DocumentOverview
          on:user={handleUser}
          {authToken}
          documents={user.documents}
        ></DocumentOverview>
      </Route>
      <Route path="/admin/login" component={AdminLogin} />
      <Route path="/auth/login/" component={Login} />
      <Route path="/auth/signup" component={Signup} />
      <Route path="/auth/reset" component={Reset} />
      {#if $notificationExpand}
        <div
          in:fly={{ x: 200, duration: 300, delay: 100 }}
          out:fly={{ x: 200, duration: 300, delay: 100 }}
          class="notification-wrapper"
          class:dark={$dark}
        >
          Hello From Notifications
        </div>
      {/if}

      {#if scan}
        <ShortcutWrapper
          {fullVerified}
          {shortcutData}
          {authToken}
          on:documentData={handleDocumentData}
          on:closeShortCut={() => {
            scan = false;
          }}
        ></ShortcutWrapper>
      {/if}

      {#if registerD}
        <ShortcutWrapper
          {fullVerified}
          {shortcutData}
          {authToken}
          routes={allDocumentPath}
          fullname={user.firstName && user.middleName && user.lastName
            ? {
                firstName: user.firstName,
                middleName: user.middleName,
                lastName: user.lastName,
              }
            : { firstName: "", middleName: "", lastName: "" }}
        ></ShortcutWrapper>
      {/if}

      {#if registerR}
        <ShortcutWrapper {fullVerified} {shortcutData} {authToken}
        ></ShortcutWrapper>
      {/if}

      {#if updateR}
        <ShortcutWrapper
          fullVerified={user.full_ver_val}
          {shortcutData}
          {authToken}
        ></ShortcutWrapper>
      {/if}
      <NavigationLocation />
    </div>
  </div>
</Router>

{#if $location === "/auth/login" || $location === "/auth/signup" || $location === "/auth/reset" || $location === "/admin/login"}
  <Footer />
{/if}

<style>
  div.side-main-wrapper {
    display: flex;

    & div.main-wrapper {
      position: relative;
      width: 100%;

      & div.notification-wrapper {
        transition: background-color ease-in-out 300ms;
        position: fixed;
        z-index: 1;
        top: 3rem;
        right: 0;
        background-color: var(--main-col-5);
        height: 95vh;
        width: 15rem;
      }

      & div.notification-wrapper.dark {
        background-color: var(--dark-main-col-5);
      }
    }
  }
</style>
