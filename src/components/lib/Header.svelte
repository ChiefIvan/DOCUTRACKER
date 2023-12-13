<script lang="ts">
  import {
    location,
    dark,
    navExpand,
    modeExpand,
    profileExpand,
    registrationExpand,
    adminUser,
  } from "../../store";
  import { tooltip } from "../shared/Tooltip";
  import { Link, navigate } from "svelte-routing";
  import { fade, fly } from "svelte/transition";
  import type { ResponseData } from "../../store";
  import { notificationExpand } from "../../store";

  import ArrowIcon from "../icons/ArrowIcon.svelte";
  import MediaQuery from "../shared/MediaQuery.svelte";
  import Mode from "../shared/Mode.svelte";
  import UserIcon from "../icons/UserIcon.svelte";
  import Button from "../shared/Button.svelte";
  import userIcon from "../../assets/user-icon.png";
  import BellIcon from "../icons/BellIcon.svelte";
  import BurgerIcon from "../icons/BurgerIcon.svelte";
  import LogoSimple from "./../../assets/transparent-favicons-simple.png";
  import DocumentAvail from "./DocumentAvail.svelte";

  export let user: ResponseData = {};
  export let verified = false;

  let img: string | undefined;

  $: {
    img = user.userImg;
  }

  const tooltipContent = "Go Back to Overview";

  const handleNavigate = () => {
    navigate("/");
  };

  const handleProfile = () => {
    $profileExpand = !$profileExpand;
    $modeExpand = false;
    $notificationExpand = false;
  };

  const handleRegistration = () => {
    $registrationExpand = true;
    $profileExpand = false;
    $notificationExpand = false;
  };

  const handleNotificationExpand = () => {
    $notificationExpand = !$notificationExpand;
    $profileExpand = false;
    $modeExpand = false;
  };

  $: if ($registrationExpand) {
    document.body.classList.add("disable-scroll");
  } else {
    document.body.classList.remove("disable-scroll");
  }
</script>

<header class="header" class:dark={$dark} class:outside={$location === "/"}>
  <div class="header-container">
    {#if $location === "/auth/login" || $location === "/auth/signup" || $location === "/auth/reset" || $location === "/admin/login"}
      <div
        class="arrow-container"
        use:tooltip={{
          arrow: false,
          content: tooltipContent,
          animation: "perspective-subtle",
          theme: "tooltip",
          offset: [0, 15],
        }}
      >
        <ArrowIcon arrowState={true} on:click={handleNavigate} />
      </div>
      <Link to="/terms">
        <span class="terms-link">Terms</span>
      </Link>
    {:else if $location === "/"}
      <div class="logo">
        <img src={LogoSimple} alt="Docutracker's Logo" />
        <h1 class:dark={$dark}>DOCUTRACKER</h1>
      </div>
      <Mode />
    {:else if $location === "/admin"}
      <div class="logo">
        <h1 class:dark={$dark}>
          Hello, Admin {$adminUser.length ? $adminUser : "Anonymous"}
        </h1>
      </div>
      <Mode />
    {:else if $location === "/dashboard" || $location === "/history" || $location === "/notifications" || $location === "/analytics" || $location === "/document/overview"}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
      <MediaQuery query="(max-width: 500px)" let:matches>
        {#if matches}
          <BurgerIcon></BurgerIcon>
        {:else}
          <DocumentAvail document={user.documents}></DocumentAvail>
        {/if}
      </MediaQuery>
      <div class="utils-wrapper">
        <div class="icon-wrapper">
          <MediaQuery query="(min-width: 500px)" let:matches>
            {#if matches}
              <BellIcon compColor={true} on:click={handleNotificationExpand} />
            {/if}
          </MediaQuery>
          <Mode />
        </div>
        {#if img && img.length !== 0}
          <!-- svelte-ignore a11y-img-redundant-alt -->
          <!-- svelte-ignore a11y-click-events-have-key-events -->
          <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
          <img
            class="user-image-profile"
            on:click|stopPropagation={handleProfile}
            src={`data:image/png;base64,${img}`}
            alt="User Profile Picture"
          />
        {:else}
          <UserIcon on:click={handleProfile} />
        {/if}
      </div>
    {/if}
  </div>
</header>

{#if $profileExpand}
  <div
    transition:fade={{ duration: 300, delay: 50 }}
    class="profiles"
    class:not-verified-wrapper={!verified}
    class:dark={$dark}
  >
    <!-- {#if verified} -->
    <div class="upper-wrapper">
      <!-- svelte-ignore a11y-img-redundant-alt -->
      {#if img && img.length !== 0}
        <img
          class="user-placeholder-icon"
          src={`data:image/png;base64,${img}`}
          alt="User Profile Picture"
        />
      {:else}
        <img class="user-placeholder-icon" src={userIcon} alt="User Icon" />
      {/if}
      <p
        transition:fly={{ y: -40, duration: 600, delay: 200 }}
        class="email-wrapper"
        class:dark={$dark}
      >
        {user.email}
      </p>
      <p
        transition:fly={{ y: -40, duration: 400, delay: 150 }}
        class="name-wrapper"
        class:dark={$dark}
      >
        Hello, {user.user_name}!
      </p>
    </div>
    <div class="button-wrapper">
      {#if user.full_ver_val}
        <Button on:click={handleRegistration} hoverized={false}
          >Edit Porfile</Button
        >
      {:else}
        <Button on:click={handleRegistration} hoverized={false}
          >Full Verification</Button
        >
      {/if}
      <MediaQuery query="(max-width: 500px)" let:matches>
        {#if matches}
          <Button on:click={() => {}} critical={true}>Logout</Button>
        {/if}
      </MediaQuery>
    </div>
    <!-- {:else} -->
    <!-- {/if} -->
  </div>
{/if}

<style>
  header.header {
    position: sticky;
    top: 0;
    z-index: 3;
    background-color: var(--header-color);
    transition: background-color ease-in-out 400ms;

    & div.header-container {
      padding: 0.5rem 1rem;
      display: flex;
      justify-content: space-between;
      align-items: center;

      & div.arrow-container {
        display: flex;
        align-items: center;
      }

      & span.terms-link {
        text-decoration: none;
        color: var(--scroll-color);
      }

      & span.terms-link:hover {
        opacity: 0.6;
        text-decoration: underline;
      }

      & div.logo {
        display: flex;
        align-items: center;
        column-gap: 0.5rem;

        & img {
          max-width: 2rem;
        }

        & h1 {
          transition: all ease-in-out 300ms;
          color: var(--scroll-color);
          font-size: 1rem;
          font-weight: bold;
        }

        & h1.dark {
          color: var(--background);
        }
      }

      & div.utils-wrapper {
        display: flex;
        align-items: center;
        column-gap: 1rem;

        & div.icon-wrapper {
          display: flex;
          gap: 0.5rem;
        }

        & img.user-image-profile {
          max-width: 2rem;
          border-radius: 50%;
        }

        & img.user-image-profile:hover {
          cursor: pointer;
        }
      }
    }
  }

  header.dark {
    background-color: var(--dark-main-col-6);
  }

  header.outside {
    background-color: transparent;
  }

  div.profiles {
    position: fixed;
    z-index: 1;
    top: 3.5rem;
    right: 0.5rem;
    padding: 1.5rem;
    border-radius: 1rem;
    box-shadow: 2px 3px 5px rgba(0, 0, 0, 0.3);
    background-color: var(--background);
    max-width: 20rem;

    & div.upper-wrapper {
      text-align: center;

      & img.user-placeholder-icon {
        max-width: -webkit-fill-available;
        border-radius: 50%;
      }

      & p.email-wrapper {
        margin: 1rem 0;
        padding: 0.5rem;
        border: 1px solid var(--main-col-6);
        color: var(--scroll-color);
        border-radius: 2rem;
        cursor: pointer;
        transition: background-color ease-in-out 300ms;
      }

      & p.email-wrapper:hover {
        background-color: var(--main-col-6);
      }

      & p.email-wrapper.dark {
        color: var(--background);
        border-color: var(--scroll-color);
      }

      & p.email-wrapper.dark:hover {
        background-color: var(--scroll-color);
      }

      & p.name-wrapper {
        margin-bottom: 0.5rem;
        font-size: 1.5rem;
        color: var(--main-col-3);
      }

      & p.name-wrapper.dark {
        color: var(--background);
      }

      & div.button-wrapper > * {
        margin-bottom: 1rem;
        /* display: flex; */
      }
    }

    /* & div.register-wrapper {
      width: 15rem;
    } */
  }

  div.dark {
    background-color: var(--dark-main-col-1);
  }
</style>
