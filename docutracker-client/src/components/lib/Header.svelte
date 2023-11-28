<script lang="ts">
  import {
    location,
    dark,
    navExpand,
    modeExpand,
    profileExpand,
    registrationExpand,
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

  export let user: ResponseData = {};
  export let userUpdatedImg: ResponseData = {};
  export let verified = false;

  let img: string | undefined;

  $: {
    img = user.userImg;
    if (userUpdatedImg.userImg?.length) {
      img = userUpdatedImg.userImg;
    }
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
</script>

<header class="header" class:dark={$dark}>
  <div class="header-container">
    {#if $location === "/auth/login" || $location === "/auth/signup" || $location === "/auth/reset"}
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
      This is Overview
    {:else if $location === "/dashboard" || $location === "/history" || $location === "/notifications" || $location === "/analytics" || $location === "/document/overview"}
      <!-- svelte-ignore a11y-click-events-have-key-events -->
      <!-- svelte-ignore a11y-no-noninteractive-element-interactions -->
      <h1 on:click={() => ($navExpand = !$navExpand)}>
        Hello, {user.user_name ? user.user_name : "Anonymous"}
      </h1>
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

  div.profiles {
    position: fixed;
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

      & div.button-wrapper {
        display: inline;
      }
    }

    & div.register-wrapper {
      width: 15rem;
    }
  }

  div.dark {
    background-color: var(--dark-main-col-1);
  }
</style>
