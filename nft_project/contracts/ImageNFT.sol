// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/utils/Counters.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

contract ImageNFT is ERC721URIStorage, Ownable {
    using Counters for Counters.Counter;
    Counters.Counter private _tokenIds;

    mapping(string => bool) private _imageHashes;

    constructor() ERC721("ImageNFT", "IMGNFT") {}

    function mintNFT(address recipient, string memory tokenURI, string memory imageHash) 
        public onlyOwner returns (uint256) {
        require(!_imageHashes[imageHash], "Image already exists");

        _tokenIds.increment();

        uint256 newItemId = _tokenIds.current();
        _mint(recipient, newItemId);
        _setTokenURI(newItemId, tokenURI);

        _imageHashes[imageHash] = true;

        return newItemId;
    }

    function verifyImage(string memory imageHash) public view returns (bool) {
        return _imageHashes[imageHash];
    }
}