<script>
  import { fly, fade } from "svelte/transition";
  import { quintInOut } from "svelte/easing";
  import { openVerSec } from "../../stores";

  import UserIcon from "../assets/userIcon.svelte";
  import Cropper from "svelte-easy-crop";

  let fileData;
  let base64String;
  let pixelCrop;
  let fileName = "";
  let croppedImage = null;
  let crop = { x: 0, y: 0 };
  let zoom = 1;

  function handleImage() {
    croppedImage = null;
    zoom = 1;
    crop = { x: 0, y: 0 };

    let files = fileData[0];
    fileName = files.name;
    const reader = new FileReader();

    reader.onload = function (e) {
      base64String = e.target.result;
    };

    reader.readAsDataURL(files);
  }

  const createImage = (url) =>
    new Promise((resolve, reject) => {
      const image = new Image();
      image.addEventListener("load", () => resolve(image));
      image.addEventListener("error", (error) => reject(error));
      image.setAttribute("crossOrigin", "anonymous");
      image.src = url;
    });

  function getRadianAngle(degreeValue) {
    return (degreeValue * Math.PI) / 180;
  }

  /**
   * @param {File} imageSrc - Image File url
   * @param {Object} pixelCrop - pixelCrop Object provided by react-easy-crop
   * @param {number} rotation - optional rotation parameter
   */
  export async function getCroppedImg(imageSrc, pixelCrop, rotation = 0) {
    const image = await createImage(imageSrc);
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    const maxSize = Math.max(image.width, image.height);
    const safeArea = 2 * ((maxSize / 2) * Math.sqrt(2));

    canvas.width = safeArea;
    canvas.height = safeArea;

    ctx.translate(safeArea / 2, safeArea / 2);
    ctx.rotate(getRadianAngle(rotation));
    ctx.translate(-safeArea / 2, -safeArea / 2);

    ctx.drawImage(
      image,
      safeArea / 2 - image.width * 0.5,
      safeArea / 2 - image.height * 0.5
    );
    const data = ctx.getImageData(0, 0, safeArea, safeArea);

    canvas.width = pixelCrop.width;
    canvas.height = pixelCrop.height;

    ctx.putImageData(
      data,
      Math.round(0 - safeArea / 2 + image.width * 0.5 - pixelCrop.x),
      Math.round(0 - safeArea / 2 + image.height * 0.5 - pixelCrop.y)
    );

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file));
      }, "image/png");
    });
  }

  export async function getRotatedImage(imageSrc, rotation = 0) {
    const image = await createImage(imageSrc);
    const canvas = document.createElement("canvas");
    const ctx = canvas.getContext("2d");

    const orientationChanged =
      rotation === 90 ||
      rotation === -90 ||
      rotation === 270 ||
      rotation === -270;
    if (orientationChanged) {
      canvas.width = image.height;
      canvas.height = image.width;
    } else {
      canvas.width = image.width;
      canvas.height = image.height;
    }

    ctx.translate(canvas.width / 2, canvas.height / 2);
    ctx.rotate((rotation * Math.PI) / 180);
    ctx.drawImage(image, -image.width / 2, -image.height / 2);

    return new Promise((resolve) => {
      canvas.toBlob((file) => {
        resolve(URL.createObjectURL(file));
      }, "image/png");
    });
  }
</script>

<div class="full-reg-container" transition:fade={{ duration: 200, delay: 0 }}>
  <section
    transition:fly={{
      x: 700,
      delay: 200,
      duration: 1000,
      easing: quintInOut,
    }}
  >
    <div class="image-wrapper">
      {#if base64String}
        <!-- svelte-ignore a11y-img-redundant-alt -->
        {#if croppedImage}
          <img
            class="final-user-picture"
            transition:fade={{ duration: 300, delay: 0 }}
            src={croppedImage}
            alt="User Image"
          />
        {:else}
          <div class="cropper-wrapper">
            <Cropper
              image={base64String}
              bind:crop
              bind:zoom
              cropShape="round"
              aspect={1}
              on:cropcomplete={(e) => (pixelCrop = e.detail.pixels)}
            />
          </div>
        {/if}
      {:else}
        <UserIcon largeSize={true} />
      {/if}

      {#if fileName.length !== 0}
        <p transition:fade={{ duration: 300, delay: 0 }}>{fileName}</p>
      {/if}
    </div>
    <form on:submit|preventDefault>
      <div class="image-wrapper">
        <label for="image_upload">Upload Your Image</label>
        <button
          on:click={async () => {
            croppedImage = await getCroppedImg(base64String, pixelCrop);
          }}>Save</button
        >
        <input
          id="image_upload"
          bind:files={fileData}
          on:change={handleImage}
          type="file"
          accept=".jpg, .jpeg, .png"
        />
      </div>
    </form>
    <button on:click={() => ($openVerSec = false)}>Close</button>
  </section>
</div>

<style>
  div.full-reg-container {
    position: fixed;
    inset: 0;
    z-index: 3;
    background-color: rgba(255, 255, 255, 0.7);
    display: flex;
    justify-content: flex-end;

    & section {
      width: 70%;
      height: 100vh;
      background-color: var(--main-col-2);
      display: flex;
      flex-direction: column;
      align-items: center;

      & div.image-wrapper {
        display: flex;
        justify-content: center;
        align-items: center;
        flex-direction: column;
        position: relative;

        & img.final-user-picture {
          width: var(--size-4);
          height: var(--size-4);

          border-radius: 50%;
        }

        & div.cropper-wrapper {
          width: var(--size-4);
          height: var(--size-4);
          position: relative;
          margin: var(--size-1) 0;
        }
      }

      & form {
        & div.image-wrapper {
          & label {
            cursor: pointer;
            display: inline-block;
            padding: var(--size-6) var(--size-3);
            background-color: var(--brdr-hovr);
            color: white;
            border-radius: var(--size-6);
          }

          & input[type="file"] {
            display: none;
          }
        }
      }
    }
  }
</style>
