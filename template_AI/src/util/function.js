export const convertLabel = (label) => {
    return label.split("_").join(" ");
}

export const numberWithCommas = (x) => {
  return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ".");
}